from bs4 import BeautifulSoup
import requests
import pandas as pd

def 수집():
    pass
# http://www.neweracapkorea.com/shop/shopbrand.html?xcode=031&mcode=002&type=Y&gf_ref=Yz1vU0FlS3M=
base_url = "http://www.neweracapkorea.com"
cap_total_url = "/shop/shopbrand.html?xcode=031&mcode=002&type=Y&gf_ref=Yz1vU0FlS3M="
base_url + cap_total_url

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
# 1~ 10 페이지 전부 다 받아오기 위한 설정
# 페이지 정보 담을 list
cap_info_list = []
price_list = []
url_list = []

for cnt in range(1,10):
    newurl = f"https://www.neweracapkorea.com/shop/shopbrand.html?type=Y&xcode=031&mcode=002&sort=&page={cnt}"
    # get으로 받아온 주소들을 공략하겠다.
    response = requests.get(base_url+cap_total_url, headers=headers) # headers를 위에 정해놓은 곳으로 선언해주기
    response.status_code # 이렇게 header로 잘 씌워야 200으로 나옴 >> 200나와야 이후 웹 크롤링이 가능

    soup = BeautifulSoup(response.content, "lxml")
    soup
    
    # 각 페이지에 있는 상품들 append, 근데 현재 사이트가 상품이 5개의 열로 표현되어 있음
    for i in range(0, 20): # 행
        for j in range(0, 5): # 열 >> 직접 맞춰줘야함
            cap_info_list.append(soup.select(f'#productClass > div > div.page-body > div.width1200 > div > table > tbody > tr:nth-child({i+2}) > td:nth-child({j+1}) > div > ul > li.dsc')[0].text)
            price_list.append(soup.select(f'#productClass > div > div.page-body > div.width1200 > div > table > tbody > tr:nth-child({i+2}) > td:nth-child({j+1}) > div > ul > li.price')[0].text)
            url_list.append(soup.select(f'#productClass > div > div.page-body > div.width1200 > div > table > tbody > tr:nth-child({i+2}) > td:nth-child({j+1}) > div > div > a')[0].attrs["href"])

print(len(cap_info_list))
print(len(price_list))
print(len(url_list))

# df화 시키기
df = pd.DataFrame(zip(cap_info_list, price_list, url_list), columns=["상품명","가격","상세페이지주소"])
# 엑셀로 저장
df.to_excel(r"C:\Users\hojun\Downloads\workspace01\data\결과물.xlsx", engine='openpyxl')
