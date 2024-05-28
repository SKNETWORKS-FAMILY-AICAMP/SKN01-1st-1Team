# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:48:23 2024

@author: Playdata
"""

import os
import time
import pandas as pd
from helpers.crawlingsele import User
import random
random.random()
from bs4 import BeautifulSoup as bs
import requests
from selenium.webdriver.common.by import By


if __name__ =='__main__':
    user = User()
    user.getBrowser('https://www.kcar.com/bc/search',new_window=True)
    user.click_button('//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[1]/div[1]/ul/li[2]/button[2]/span/i') # 정렬버튼
    user.scroll_down(200)
    time.sleep(random.random())

    # user.click_button('//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[3]/div/ul/li[12]/button')
    # user.scroll_down(200) #다음페이지버튼
    # time.sleep(random.random())

    # 페이지전체 싹긁음
    txt = '/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[4]/div[1]/div[6]'
    data = user.find_ele_text(txt)
    user.scroll_down(50)
    user.close_connect()

    aa=list(data.split('\n'))        
    remove_set = {'비교함에 담기',}  #필요없는정보버림
    aa2 = [i for i in aa if i not in remove_set]  #시간복잡도좋게처리
    aa3 = [i for i in aa2 if '타임딜' not in i]  #위랑비슷함
    tmp=[]
    tmp2=[]
    for i in aa3:
        if i == "찜하기":  #이걸구분으로2차원리스트만듬
            tmp2.append(tmp)
            tmp=[]
        else:
            tmp.append(i)
    tmp2.pop(0)  #첫번째원소비어있어서버림
    
    for i in range(len(tmp2)):
        tmp2[i] = tmp2[i][:5] #정보 5개만 담도록 정리함
    
    df = pd.DataFrame(data=tmp2,columns=['차종','금액','할부','연식','주행거리'])
    df.to_excel(os.getcwd()+"케이카.xlsx",index=False)
    
# //*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[3]/div/ul/li[3]/span
# 1제목 /html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[4]/div[1]/div[6]/div[1]/div/div[2]/div[1]/p/a
# 2제목 /html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[4]/div[1]/div[6]/div[2]/div/div[2]/div[1]/p/a

    # for i in range(2,12):  # 리뷰관련 크롤링 하려다가 스톱함
        # headline = f'/html/body/div[1]/div/div/div[2]/div[1]/div/div[{i}]/ul/li[1]/a/span/h5'
        # detail = f'/html/body/div[1]/div/div/div[2]/div[1]/div/div[{i}]/ul/li[1]/a/span/p'
# /html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/ul/li[1]/a/span/h5  제목1
# /html/body/div[1]/div/div/div[2]/div[1]/div/div[3]/ul/li[1]/a/span/h5  제목2
# /html/body/div[1]/div/div/div[2]/div[1]/div/div[11]/ul/li[1]/a/span/h5  제목끝1p
# f'/html/body/div[1]/div/div/div[2]/div[1]/div/div[{i}]/ul/li[1]/a/span/h5'
# /html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/ul/li[1]/a/span/p  본문1
# /html/body/div[1]/div/div/div[2]/div[1]/div/div[3]/ul/li[1]/a/span/p  본문2
# /html/body/div[1]/div/div/div[2]/div[1]/div/div[11]/ul/li[1]/a/span/p  본문끝1p
# f'/html/body/div[1]/div/div/div[2]/div[1]/div/div[{i}]/ul/li[1]/a/span/p'
    
from db.dbwork import DB
import pymysql.cursors
# Establish a connection to your MySQL server.
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='')
try:
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE mydatabase")
finally:
    connection.close()


import pandas as pd
from sqlalchemy import create_engine
# 엑셀 파일 읽기
df_read = pd.read_excel(os.getcwd()+"케이카.xlsx")


# # MySQL 데이터베이스 연결 정보
# db_host = 'localhost'
# db_user = 'Playdata'
# db_password = ''
# db_name = 'used_cars'

# # 데이터베이스 연결 문자열 생성
# db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"

# # 엑셀 파일 경로
# excel_file = 'example.xlsx'

# # 엑셀 파일 읽기
# df = pd.read_excel(excel_file)

# # MySQL 데이터베이스 연결
# engine = create_engine(db_url)

# # 데이터프레임을 MySQL 데이터베이스 테이블에 삽입
# df.to_sql('table_name', engine, if_exists='replace', index=False)

# # 데이터베이스 연결 종료
# engine.dispose()












