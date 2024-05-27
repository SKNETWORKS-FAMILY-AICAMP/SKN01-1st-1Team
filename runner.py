#from helpers.db import MySQLDatabase
from helpers.db2 import record_insert
# from helpers.ui import Ms # streamlit 용도
# from helpers.crawling import 수집

if __name__ == "__main__":
    # 크롤링하는 클래스
    # 수집()

    # 03 db에 저장

    # try:
    #     user = "root"
    #     password = ""
    #     host = "localhost"
    #     port = 3306
    #     db = "test"

    #     db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    #     db = MySQLDatabase(db_url)

    #     import sys
    #     sys.exit()
    #     print(db.__repr__)
        
    #     # db결과를 파일로 저장하는 method(to_sql)를 MySQLDatabase 클래스에 추가
    #     db.to_sql
        
    #     #db.add_user("john_doe", "john@example.com")
    #     #user =  db.get_user_by_username("john_doe")
    #     #print(user.username, user.email)
    #     #db.update_user_email("john_doe", "new_email@example.com")
    #     #user =  db.get_user_by_username("john_doe")
    #     # print(user.username, user.email)
    #     # db.delete_user("john_doe")

    # except Exception as e:
        # print("DB부분처리안됨")    
        # print("e")

    # 04 db2로 저장
    record_insert()

    # 스트림릿 클래스
