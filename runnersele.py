#from helpers.db import MySQLDatabase
from helpers.dbsele import *
#from helpers.crawling import 수집
from helpers.crawlingsele import User
import pandas as pd
import time
import os

if __name__ == "__main__":
    # 125.0.6422.113 # 현재 크롬 드라이버 버전
    
    # 드라이버 버전 맞춰주기 60에서 125.0.6422.113 으로
    # https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/win64/chromedriver-win64.zip
    # https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.113/win64/chromedriver-win64.zip
    
    user = User("n") # 다나와
    user.페이지이동("https://www.danawa.com/")
    
    # 작업을 넣어줌 (검색어창 뜯어봄)
    # AKCSearch # css.selector방식
    # //*[@id="AKCSearch"] # xpath 방식
    user.객체선택값입히기('//*[@id="AKCSearch"]', "맥북") # 검색어창에 맥북이라 자동으로 입력됨
    user.delay(3)
    # 맥북 입력 상태에서 검색기능 클릭
    user.객체선택하고클릭('//*[contains(concat( " ", @class, " " ), concat( " ", "search__submit", " " ))]') # xpath 꼭 클릭하기
    user.delay(3)
    # //*[@id="saveDESC"]/a # 인기 상품 순의 체크박스표시 xpath
    # //*[@id="opinionDESC"]/a # 상품평 많은 순의 체크박스 xpath
    user.객체선택하고클릭('//*[@id="opinionDESC"]/a') # 맥북 검색기록중 상품평 많은 순 클릭
    time.sleep(1) # 이래야 팝업떠도 에러가 안 남, delay함수보단 sleep으로 exlplicit하게 딜레이주기
    # 상품평 많은 순 중 첫 상품 >> iter 가능
    # //*[@id="productItem12660491"]/div/div[2]/p/a => 첫 번째 상품은 2로 타겠구나 div[2]
    # 상품명 말고 그림을 클릭해서 페이지 전환하도록? //*[@id="thumbLink_12660491"]
    user.객체선택하고클릭('//*[@id="thumbLink_12660491"]') # 첫 상품 클릭 >> 여기서 에러나네
    time.sleep(1)
    # 클릭한 물품의 상세페이지 생성 => 새로운 창(객체)이 생김 >> 이전 객체와 달라지는데?
    # 셀레니움 새창 제어 검색 : https://staedtler1207.tistory.com/10 참고
    user.새창으로활성이동(1)
    user.delay(1)
    # 새 창에서 객체선택하고 클릭해보기 
    #user.객체선택하고클릭('//*[@id="danawa-prodBlog-newsRoom-item-5528681"]') # 해당 상품에 대한 뉴스들
    # 안 되면 페이지 다운버튼 기능 수행
    # 쇼핑몰 상품리뷰 탭 클릭
    user.객체선택하고클릭('//*[(@id = "danawa-prodBlog-productOpinion-button-tab-companyReview")]//*[contains(concat( " ", @class, " " ), concat( " ", "txt", " " ))]')
    time.sleep(1)
    # 첫번째 리뷰
    review = user.객체선택('//*[@id="danawa-prodBlog-companyReview-content-wrap-0"]/div/div[1]/p')
    print("title : ", review)
    
    product = []
    title = []
    text = []
    page = []
    # 여러 리뷰
    for i in range(10): # 페이지 넘어가는 기능
        time.sleep(1)
        for j in range(10): # 한 페이지의 상품 리뷰
            product.append("맥북")
            title.append(user.객체선택(f'//*[@id="danawa-prodBlog-companyReview-content-wrap-{j}"]/div/div[1]/p'))
            text.append(user.객체선택(f'//*[@id="danawa-prodBlog-companyReview-content-wrap-{j}"]/div/div[2]'))
            # 다음 페이지 클릭
            #user.paging(f'/html/body/div[2]/div[5]/div[2]/div[4]/div[4]/div/div[3]/div[2]/div[3]/div[2]/div[5]/div/div/div/a{i+2}')
        #page.append(i+1)
    # print(title)
    # print(text)
    time.sleep(3) # 잘 보기위해 n초정도 보기

    df = pd.DataFrame(
        data=zip(product, title, text),
        columns=["상품명", "제목", "리뷰내용"]
    )
    df.to_excel(r"C:\Users\hojun\Downloads\workspace01\data\다나와.xlsx")

    # 테이블로 레코드 인서트 ?
    record_insert(os.path.join(r"C:\Users\hojun\Downloads\workspace01\data\다나와.xlsx"))