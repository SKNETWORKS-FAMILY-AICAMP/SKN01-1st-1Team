import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt # 차트다루기 위한 외부 라이브러리
import seaborn as sns # 차트관련 라이브러리 (좀 더 잘 꾸며주는 역할?)
import numpy as np

# matplotlib는 한글폰트 적용시 문제가 있어 항상 하는 세팅이 있음
# 한글폰트 설정
# Windows, 리눅스 사용자
plt.rcParams['font.family'] = "NanumGothic"
plt.rcParams['axes.unicode_minus'] = False

# MAC 사용자
# plt.rcParams['font.family'] = "AppleGothic"

# dataframe 생성
data = pd.DataFrame({
    '이름': ['영식','철수','영희'],
    '나이': [22,31,25],
    '몸무게': [75.5,80.2,55.1]
})

st.dataframe(data, use_container_width=True)

fig, ax = plt.subplots() # subplots 2개를 튜플형식으로 반환
# ax에 bar 차트를 넣겠다. (x,y 축만 존재 >> 2개만 입력됨)
ax.bar(data['이름'], data['나이']) # data에 있는 이름들을 출력 -> series 형식으로 출력

# ax에 pie, line차트 넣기 >> 근데 2개 입력은 안 되는 듯?
# ax.pie(data['이름'], data['나이'])

# streamlit에서 차트 그리는 method pyplot
st.pyplot(fig)

# barplot 만들기 : data는 pandas 형식이어야함, ax는 축 설정 어케할것인지
# legend : 전설, (범례) >> 어디에 범례를 줄까만 정해주면 됨
barplot = sns.barplot(x='이름', y='나이', data=data, ax=ax, palette='Set2', legend="auto")

fig = barplot.get_figure()
st.pyplot(fig)