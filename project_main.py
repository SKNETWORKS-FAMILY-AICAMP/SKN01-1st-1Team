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
    user.페이지이동("https://www.kcar.com/bc/search")
    
    model = [] # 자동차 모델명
    price = [] # 자동차 가격
    olders = [] # 연식
    km = [] # 달린 거리
    energy = [] # 필요한 연료
    location = [] # 파는 장소
    
    # 모든 페이지 크롤링
    cnt = 0
    for i in range(1):# 121:
        #time.sleep(1)
        user.delay(1)
        # > 버튼으로 다음 페이지 넘어가기
        user.click_button(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[3]/div/ul/li[12]/button')
        for j in range(1,10): # 페이지 넘어가는 기능 (여기서 객체, 페이지넘버 순환)
            #time.sleep(1)
            user.delay(1)
            model.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[1]/p'))
            price.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[2]/div/p'))
            olders.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[2]/p/span[1]'))
            km.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[2]/p/span[2]'))
            energy.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[2]/p/span[3]'))
            location.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[2]/p/span[4]'))
        # time.sleep(1) # 잘 보기위해 n초정도 보기
        user.delay(3)

    df = pd.DataFrame(
        data=zip(model, price,olders,km,energy,location),
        columns=["모델명", "가격","연식","주행 거리", "연료", "거래 장소"]
    )
    # 너의 경로 입력
    df.to_excel(r"C:\Users\Playdata\Downloads\협업\SKN01-1st-1Team\data\케이카.xlsx")

    # 테이블로 레코드 인서트
    record_insert(os.path.join(r"C:\Users\Playdata\Downloads\협업\SKN01-1st-1Team\data\케이카.xlsx"))
    
    # 파이썬과 db연동해서 crud 실행 
    # try:
    #     user = "root"
    #     password = ""
    #     host = "localhost"
    #     port = 3306
    #     db = "project"

    #     db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    #     db = MySQLDatabase(db_url)

    #     # 변수 = eval(변수) : eval 기능 객체화시켜줌 >> 보안적으로 문제가 되어 사용 권장은 x
    #     # 이걸 활용하면 동적 변수로서 사용가능 하지만  __repr__ 을 활용하자
    #     print(db.__repr__)
    #     db.add_user("john_doe", "john@example.com")
    #     user =  db.get_user_by_username("john_doe")

    # except Exception as e:
    #     print("DB부분처리안됨")    
    #     print("e")