

def record_insert():
    import pandas as pd

    df = pd.read_excel(r"C:\Users\hojun\Downloads\workspace01\data\모자결과물.xlsx")

    import pymysql.cursors

    connection = pymysql.connect(host='localhost', user='root', password='', db='test')
    상품명 = df["상품명"][0]
    가격 = df["가격"][0] # 난 그냥 db table varchar로 해서 해결
    # db에서 가격을 int로 설정했다면
    # 가격 = df["가격"][0]
    # 가격.replace("원","").replace(",","")
    # int(가격)
    링크 = df["상세페이지주소"][0]

    try:
        with connection.cursor() as cursor:
            # test db의 crawlilng table에 해당 정보 입력
            cursor.execute("INSERT INTO crawling (itemname, price, link) VALUES ('{}','{}','{}')".format(상품명, 가격, 링크))
            connection.commit()
    finally:
        connection.close()
    print("인서트 1개 됨")
