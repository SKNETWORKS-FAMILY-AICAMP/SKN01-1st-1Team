# selenium으로 사이트 뜯기

# from helpers.db import MySQLDatabase
# from helpers.dbsele import *
# from helpers.crawling import 수집
# from helpers.crawlingsele import User
from 셀레니움모듈 import User
import pandas as pd
import time
import os

if __name__ == "__main__":
    user = User("n")  # k car 사이트
    user.페이지이동("https://www.kcar.com/bc/search")
    model = []
    price = []
    # 여러 리뷰
    cnt = 0
    for i in range(10):
        time.sleep(1)

        user.click_button(
            f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[3]/div/ul/li[12]/button'
        )
        for j in range(1, 10):  # 페이지 넘어가는 기능 (여기서 객체, 페이지넘버 순환)
            # time.sleep(1)
            user.delay(1)
            model.append(
                user.객체선택(
                    f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[1]/p'
                )
            )
            price.append(
                user.객체선택(
                    f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{j}]/div[2]/div[2]/div/p'
                )
            )
        # time.sleep(1) # 잘 보기위해 n초정도 보기
        user.delay(3)
        # 다음페이지 넘어가기

    # //*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[1]/div[2]/div[2]/p/span[2]
    # //*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/p/span[2]
    # f'//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[2]/div[2]/div[{i}]/div[2]/div[2]/p/span[2]'

    df = pd.DataFrame(data=zip(model, price), columns=["모델명", "가격", "주행거리"])
    df.to_excel(
        r"C:\Users\Playdata\Downloads\프로젝트\다나와_리뷰_크롤링 - 케이카조회를시도중\케이카.xlsx"
    )
    # 테이블로 레코드 인서트 ?
    # record_insert(os.path.join(r"C:\Users\hojun\Downloads\workspace01\data\엔카.xlsx"))
