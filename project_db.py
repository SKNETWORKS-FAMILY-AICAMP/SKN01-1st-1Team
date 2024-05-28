from helpers.dbsele import *
import os

if __name__ == "__main__":
    # 테이블로 레코드 인서트
    try:
        user = "root"
        password = ""
        host = "localhost"
        port = 3306
        dbname = "project"
        
        table = "review" # 넣을 table 잘 설정해주기 <=> record_insert와 호환

        db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"
        record_insert(os.path.join(os.getcwd() + "\\data\\리뷰.xlsx"), db_url, table)
        #record_insert(os.path.join(os.getcwd() + "\\data\\케이카_원본.xlsx")db_url, table)
        #record_insert(os.path.join(os.getcwd() + "\\data\\FAQ_원본.xlsx")db_url, table)

        # 파이썬과 db연동해서 crud 실행 
        #db = MySQLDatabase(db_url)
        # print(db.__repr__)
        # db.add_user("john_doe", "john@example.com")
        # user =  db.get_user_by_username("john_doe")

    except Exception as e:
        print("DB부분처리안됨")    
        print("e")

