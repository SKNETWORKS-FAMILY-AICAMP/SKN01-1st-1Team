# selenium으로 사이트 뜯기

#from helpers.db import MySQLDatabase
from helpers.dbsele import *
#from helpers.crawling import 수집
from helpers.crawlingsele import User
import pandas as pd
import time
import os

if __name__ == "__main__":

    user = User("n") # k car 사이트
    user.페이지이동("https://www.kcar.com/bc/review/BuyCustReview")
    
    title = [] # 제목
    review = [] # 내용
    model = [] # 차종
    date = [] # 날짜
    image = [] # 이미지 ?
    
    # 모든 페이지 크롤링
    cnt = 0
    for i in range(14):
        #time.sleep(1)
        user.delay(1)
        # > 버튼으로 다음 페이지 넘어가기
        user.click_button(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[3]/div/ul/li[12]/button')
        for j in range(1,10): # 페이지 넘어가는 기능 (여기서 객체, 페이지넘버 순환)
            #time.sleep(1)
            user.delay(1)
            title.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[1]/p'))
            review.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[2]/div/p'))
            model.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[2]/p/span[1]'))
            date.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[2]/p/span[2]'))
            # image.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[2]/p/span[2]'))
        # time.sleep(1) # 잘 보기위해 n초정도 보기
        user.delay(3)

    df = pd.DataFrame(
        data=zip(title, review, model, date),
        columns=["제목", "내용", "차종", "리뷰 날짜"]
    )
    # 너의 경로 입력
    df.to_excel(r"C:\Users\hojun\Downloads\workspace01\data\리뷰.xlsx")

    # # 테이블로 레코드 인서트
    # record_insert(os.path.join(r"C:\Users\hojun\Downloads\workspace01\data\리뷰.xlsx"))

