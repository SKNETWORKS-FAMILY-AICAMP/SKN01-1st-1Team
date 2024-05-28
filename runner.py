import os
import time
import pandas as pd
from helpers.crawlingsele import User

import random
random.random()
from bs4 import BeautifulSoup as bs
import requests
def fetch_webpage(url):
    try:
        response = requests.get(url)
        # HTTP 응답 상태코드가 200 OK인 경우에만 데이터 반환
        if response.status_code == 200:
            return response.text
        else:
            print("Error:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None


if __name__ =='__main__':
    user = User()
    user.getBrowser('https://www.kcar.com/bc/search',new_window=True)
    user.click_button('//*[@id="app"]/div[2]/div[2]/div[2]/div[4]/div[1]/div[1]/ul/li[2]/button[2]/span/i') # 정렬버튼
    # user.scroll_down() # 내려서
    user.scroll_down(200)
    time.sleep(random.random())
    
    url = 'https://www.kcar.com/bc/search'
    txt = fetch_webpage(url)
    print(txt)
    bs = bs(txt, 'html.parser')



    # rev_lst = []
    # star_lst = []
    # for i in range(6):
    #     try:
    #         for j in range(10): # 제목이나 사이트 등 더 추가하고 싶다면 여기서 추가 입력
    #             txt = f'/html/body/div[2]/div[5]/div[2]/div[4]/div[4]/div/div[3]/div[2]/div[3]/div[2]/div[5]/ul/li[{j+1}]/div[2]/div/div[2]' # 본문
    #             star = f'/html/body/div[2]/div[5]/div[2]/div[4]   /div[4]/div/div[3]/div[2]/div[3]/div[2]/div[5]/ul/li[{j+1}]/div[1]/span[1]/span' # 별점
    #             txt = user.find_ele_text(txt)
    #             print(txt)
    #             star = user.find_ele_text(star)
    #             print(star)
    #             rev_lst.append(txt)
    #             star_lst.append(star)
    #     except :
    #         break
    #     if i == 5:
    #         user.click_button('/html/body/div[2]/div[5]/div[2]/div[4]/div[4]/div/div[3]/div[2]/div[3]/div[2]/div[5]/div/div/div/span')
    #     else :
    #         print(f'------------ {i+1}번 finished!! -------------')
    #         time.sleep(2)
    #         user.click_button(f'/html/body/div[2]/div[5]/div[2]/div[4]/div[4]/div/div[3]/div[2]/div[3]/div[2]/div[5]/div/div/div/a[{i+1}]')
    #         time.sleep(5)    
        
    user.close_connect()
    # print(f'리뷰 {len(rev_lst)}개, 별점 {len(star_lst)}개가 저장되었습니다.')

    # df = pd.DataFrame({'리뷰':rev_lst, '별점':star_lst})
    # # result 파일 경로 만들기
    # result_path = os.path.join(os.getcwd(),'result')
    # os.makedirs(result_path, exist_ok=True)
    # # csv로 저장
    # df.to_csv(os.path.join(result_path,'review.csv'), index=False, encoding='utf-8')
    # print(f'#### "review.csv"가 {result_path}에 저장되었습니다. ####')