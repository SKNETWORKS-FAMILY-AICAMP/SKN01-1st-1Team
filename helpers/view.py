import streamlit as st
from streamlit.components.v1 import html
import numpy as np
import pandas as pd
import pymysql
import datetime
import matplotlib.pyplot as plt
import altair as alt
from datetime import datetime as dt

# st.set_page_config(layout="wide")


font_path = r"C:\Windows\Fonts\batang.ttc"
font_name = plt.matplotlib.font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams["font.family"] = font_name
plt.rc("font", family=font_name)
plt.rcParams["axes.unicode_minus"] = False


class View:

    def __init__(self, appname):

        def fetch_data_from_database(tablename):
            # MySQL 데이터베이스에 연결
            connection = pymysql.connect(
                host=host, user=user, password=password, db=db_name
            )

            # 쿼리 실행
            query = f"SELECT * FROM {tablename};"
            data = pd.read_sql(query, connection)

            # 연결 닫기
            connection.close()
            data = data.iloc[:, 1:]

            return data

        st.title(appname)

        host = "localhost"
        user = "encore"
        password = "encore1234"
        db_name = "used_car"

        option = st.sidebar.selectbox(
            "Menu",
            (
                "K-car 중고차 목록",
                "K-car 리스 차 목록",
                "K-car 리뷰 목록",
                "K-car FAQ 목록",
                "graph",
            ),
        )

        data1 = fetch_data_from_database("carlist")

        if option == "K-car 중고차 목록":
            st.subheader("K-car 중고차 목록")

            # st.write(data1)

            filtered_df = data1

            col1, col2, col3 = st.columns(3)

            with col1:
                search_name = st.text_input("모델명 검색")
            with col2:
                selected_gas = st.multiselect(
                    "연료 선택", options=filtered_df["연료"].unique()
                )
            with col3:
                selected_place = st.multiselect(
                    "거래장소 선택", options=filtered_df["거래장소"].unique()
                )

            min_price = filtered_df["가격"].min()
            max_price = filtered_df["가격"].max()
            selected_price = st.slider(
                "금액 범위를 선택하세요 (단위: 만원)",
                min_value=min_price,
                max_value=max_price,
                value=(min_price, max_price),
            )

            min_distance = filtered_df["주행거리"].min()
            max_distance = filtered_df["주행거리"].max()
            selected_distance = st.slider(
                "주행거리 범위를 선택하세요 (단위: km)",
                min_value=min_distance,
                max_value=max_distance,
                value=(min_distance, max_distance),
            )

            if search_name:
                filtered_df = filtered_df[
                    filtered_df["모델명"].str.contains(
                        search_name, case=False, na=False
                    )
                ]
            if selected_gas:
                filtered_df = filtered_df[filtered_df["연료"].isin(selected_gas)]
            if selected_place:
                filtered_df = filtered_df[filtered_df["거래장소"].isin(selected_place)]
            else:
                filtered_df = filtered_df

            filtered_df = filtered_df[
                (filtered_df["가격"] >= selected_price[0])
                & (filtered_df["가격"] <= selected_price[1])
            ]

            filtered_df = filtered_df[
                (filtered_df["주행거리"] >= selected_distance[0])
                & (filtered_df["주행거리"] <= selected_distance[1])
            ]

            st.write(filtered_df)

        elif option == "K-car 리스 차 목록":
            st.subheader("K-car 리스 차 목록")
            data2 = fetch_data_from_database("leasecarlist")
            st.write(data2)

        elif option == "K-car 리뷰 목록":
            st.subheader("K-car 리뷰 목록")
            data3 = fetch_data_from_database("review")
            st.write(data3)

        elif option == "K-car FAQ 목록":
            st.subheader("K-car FAQ 목록")
            data4 = fetch_data_from_database("faq")
            st.write(data4)

        elif option == "graph":
            가격 = []
            연료 = []

            for i in range(1000):
                가격.append(data1.가격[i])
                연료.append(data1.연료[i])

            # 히스토그램 데이터를 얻기 위해 bins를 계산합니다.
            counts, bins = np.histogram(가격, bins=30)

            # 히스토그램 데이터를 데이터프레임으로 변환합니다.
            hist_data = pd.DataFrame({"가격": bins[:-1], "중고차 수": counts})

            # # 정규분포 그래프를 Streamlit 앱에 표시
            st.header("중고차 가격대별 분포 그래프")
            st.line_chart(hist_data.set_index("가격"), use_container_width=True)

            labels = "디젤", "가솔린", "가솔린+전기", "전기", "디젤+전기"
            sizes = [
                연료.count("디젤"),
                연료.count("가솔린"),
                연료.count("가솔린+전기"),
                연료.count("전기"),
                연료.count("디젤+전기"),
            ]
            explode = (0, 0.1, 0, 0, 0)

            fig1, ax1 = plt.subplots()
            ax1.pie(
                sizes,
                explode=explode,
                labels=labels,
                autopct="%1.1f%%",
                shadow=True,
                startangle=45,
            )
            ax1.axis(
                "equal"
            )  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.header("중고차 사용 연료 비율 그래프")
            st.pyplot(fig1)
