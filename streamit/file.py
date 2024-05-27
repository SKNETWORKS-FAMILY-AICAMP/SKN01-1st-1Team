import streamlit as st
import pandas as pd
import time

# 파일 업로드 버튼
file = st.file_uploader("파일 선택(csv or excel)", type=['csv','xls','xlsx'])

# 파일이 정상 업로드 된 경우
if file is not None:
    # 파일 읽기
    df = pd.read_csv(file)
    # pandas 형식의 데이터 출력
    st.dataframe(df) 

# tile.sleep(3) # 왜 딜레이를 줄까?

# excel or CSV 확장자를 구분하여 출력하는 경우
if file is not None:
    # st 객체인 file의 맨 끝 이름인 확장자 가져오기
    ext = file.name.split('.')[-1]

    if ext == 'csv':
        # 파일 읽기
        df = pd.read_csv(file)
        st.dataframe(df) # 출력
    elif 'xls' in ext:
        df = pd.read_excel(file, engine='openpyxl')
        st.dataframe(df) # 출력