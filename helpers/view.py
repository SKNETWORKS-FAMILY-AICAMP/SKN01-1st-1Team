import streamlit as st
from streamlit.components.v1 import html
import numpy as np
import pandas as pd
import pymysql
import datetime
from datetime import datetime as dt


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

            return data

        st.title(appname)

        host = "localhost"
        user = "encore"
        password = "encore1234"
        db_name = "used_car"

        st.subheader("K-car 중고차 목록")
        data1 = fetch_data_from_database("carlist")
        st.write(data1)

        st.subheader("K-car FAQ 목록")
        data2 = fetch_data_from_database("faq")
        st.write(data2)

        dataframe = pd.DataFrame(data1)

        st.plotly_chart(dataframe)

        # Streamlit 앱 제목

        # 데이터를 테이블로 출력
        
