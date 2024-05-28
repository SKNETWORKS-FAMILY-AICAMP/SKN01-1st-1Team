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
        table = "review"
        db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"
        record_insert(os.path.join(r"C:\Users\hojun\Downloads\workspace01\data\리뷰_원본.xlsx"), db_url, table)
        #record_insert(os.path.join(r"C:\Users\hojun\Downloads\workspace01\data\케이카_원본.xlsx"))
        #record_insert(os.path.join(r"C:\Users\hojun\Downloads\workspace01\data\FAQ_원본.xlsx"))

        # 파이썬과 db연동해서 crud 실행 
        #db = MySQLDatabase(db_url)
        # print(db.__repr__)
        # db.add_user("john_doe", "john@example.com")
        # user =  db.get_user_by_username("john_doe")

    except Exception as e:
        print("DB부분처리안됨")    
        print("e")

