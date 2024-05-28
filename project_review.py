# selenium으로 사이트 뜯기

from helpers.dbsele import *
from helpers.crawlingsele import User
import pandas as pd
import time, os

if __name__ == "__main__":
    user = User("n") # k car 사이트
    user.페이지이동("https://www.kcar.com/bc/review/BuyCustReview")
    
    title = [] # 제목
    review = [] # 내용
    model = [] # 차종
    date = [] # 날짜

    cnt = 0
    for i in range(14):
        user.delay(1)
        for j in range(1,9): # 8개의 리뷰 클릭
            # 리뷰 박스 클릭
            user.객체선택하고클릭(f'//*[@id="app"]/div[2]/div[1]/div/div[{j+1}]/ul')
            time.sleep(1)
            title.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/h5'))
            review.append(user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/p'))
            # 차종, 날짜 같이 선택되는 것 분리
            model_date = user.객체선택(f'//*[@id="app"]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div/span')
            mo, da = model_date[:-10], model_date[-10:]
            model.append(mo)
            date.append(da)
            
            # 다 넣었다면 리뷰창 나가기 (x창 눌러서)
            user.click_button(f'//*[@id="app"]/div[2]/div[2]/div/div/div[1]/button')
        user.delay(3)
        # 다음 페이지 넘어가기
        # 10개 씩일땐 li[12]인데 마지막즘 되면 그거에 맞게끔 순회해야함 여기의 경우 14번까지라, 10번 넘어가면 li[6]이 우클릭
        if i < 11:
            user.click_button(f'//*[@id="app"]/div[2]/div[1]/div/div[12]/div/ul/li[12]/button')
        else:
            user.click_button(f'//*[@id="app"]/div[2]/div[1]/div/div[12]/div/ul/li[6]/button')

    df = pd.DataFrame(
        data=zip(title, review, model, date),
        columns=["제목", "내용", "차종", "리뷰 날짜"]
    )
    # 너의 경로 입력 (os.getcwd()를 통해 각자 경로다른 사람들이 써도 사용 가능하도록)
    df.to_excel(os.getcwd() + "\\data\\리뷰.xlsx", index=False)

