import streamlit as st
import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt

class View:
    def __init__(self, appname):
        # dataframe 생성
        # 이렇게 직접적으로 넣어도 되고, 간접적으로 변수받고 넣어도 됨
        dataframe = pd.DataFrame(        {
            'first column' : [1,2,3,4],
            'second column' : [10,20,30,40],
        }) 
        # 기본적으로 정수형 index 0 ~ , str로 만들 수 있음
        st.dataframe(dataframe, use_container_width=False)
        # 고정된 table >> 다른것과 연동 x, 위의 dataframe은 클릭을 통해 정렬도 됨
        st.table(dataframe)

        # vector(1차원), matrix, tensor
        st.metric(label="온도", value="10ºC", delta="1.2ºC")
        st.metric(label="삼성전자", value="61,000원", delta="-1,200원")
        
        col1, col2, col3 = st.columns(3) # 열을 몇등분 하겠다.
        # 나눈 컬럼들 별로 
        col1.metric(label="삼성전자", value="62,000원", delta = "1,000원")
        col2.metric(label="LG전자", value="61,000원", delta = "900원")
        col3.metric(label="대우전자", value="63,000원", delta="800원")

        # 예제 02 basic-ui
        button = st.button("눌러주세요")
        button2 = st.button("되돌리기")
        if button: # button == True
            st.write(":blue[버튼]이 눌렸습니다. :sparkles:")
        if button2:
            # write하기 보단 객체의 value를 없애는 쪽으로
            pass
        
        # 파일 다운로드
        st.download_button(
            label='csv로 다운로드', # db와 연동 후 csv로 다운로드하는 식으로
            data=dataframe.to_csv(), # pandas의 to_csv 기능
            file_name='sample.csv',
            mime='text/csv'
        )

        # 체크박스
        agree = st.checkbox("동의?")
        if agree:
            st.write("감사합니다. :smile:")
        
        # mbti 테스트
        mbti = st.radio('MBTI?',('ENFP','ISTJ'))
        mbti2 = st.selectbox('MBTI?',('ISTJ','ENFP'),index=0)
        mbti3 = st.multiselect('MBTI?',('ISTJ','ISTP','ENFP'))
        # 범위 설정
        values = st.slider(
            '선택해주세요',
            0.0, 100.0, (25.0, 75.0)
        )

        start_time = st.slider(
            "언제 약속을 잡을까요?",
            min_value=dt(2020,1,1,0,0),
            max_value=dt(2020,1,7,23,0),
            value=dt(2020,1,3,12,0),
            step=datetime.timedelta(hours=1),
            format="MM/DD/YY - HH:mm")
        st.write("선택한 약속 시간:",start_time)

        # 텍스트 입력 (중요)
        title = st.text_input(label="나이 입력",
                              placeholder=20)
        title = st.number_input(label="나이 입력",
                                min_value=0,
                                max_value=100,
                                placeholder=20, step=1)
        