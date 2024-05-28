# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:09:36 2024
케이카_원본.xlsx 데이터베이스 VARCHAR 를 INT로 쓸 수 있게 처리 
@author: 최명근
"""
import os
import pandas as pd

df_read = pd.read_excel(os.getcwd()+"\\data\\케이카_원본.xlsx", )
df_read = df_read.drop(df_read.columns[0],axis=1)


df_CarFullPrice = df_read[~df_read['가격'].str.startswith('리스')]
df_CarLesPrice = df_read[df_read['가격'].str.contains('리스')]


df_CarFullPrice['가격'] = df_CarFullPrice['가격'].replace({'[^0-9]': ''}, regex=True)
df_CarFullPrice['주행 거리'] = df_CarFullPrice['주행 거리'].replace({'[^0-9]': ''}, regex=True)

df_CarLesPrice['주행 거리'] = df_CarLesPrice['주행 거리'].replace({'[^0-9]': ''}, regex=True)


df_CarFullPrice.to_excel(os.getcwd()+"\\data\\케이카_금액거리처리.xlsx",index=False)
df_CarLesPrice.to_excel(os.getcwd()+"\\data\\케이카_리스만+금액거리처리.xlsx",index=False)
