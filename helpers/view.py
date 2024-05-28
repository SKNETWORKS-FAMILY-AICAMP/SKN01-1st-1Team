import streamlit as st
from streamlit.components.v1 import html
import numpy as np
import pandas as pd
import pymysql
import datetime
import plotly.express as px
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

        # 순번 = []
        # 연료 = []

        # for i in range(1000):
        #     순번.append(data1.id[i])
        #     연료.append(data1.연료[i])

        # chartdata = {
        #     '순번' : 순번,
        #     '연료' : 연료
        # }
        # cd = pd.DataFrame(chartdata)

        # fig = px.pie(cd, name='순번', values='연료', 
	    # title='K-car중고차 연료타입', hole=.3) # hole을 주면 donut 차트

        # fig.update_traces(textposition='inside', textinfo='percent+label+value')
        # fig.update_layout(font=dict(size=14))
        # fig.update(layout_showlegend=False) # 범례표시 제거

        # st.plotly_chart(fig)

        # Streamlit 앱 제목

        # 데이터를 테이블로 출력
        
