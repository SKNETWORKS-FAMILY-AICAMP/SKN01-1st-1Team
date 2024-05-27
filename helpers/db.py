# 디비로 저장한다. => 수집 될 때 마다 한다.
from sqlalchemy import engine, create_engine, DateTime, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import pandas as pd

Base = declarative_base() # 실제 테이블에 선언되어 있는 방식으로 받아들이겠다.

# table은 프로젝트에 맞게 다시 재구성하기
class Tausers(Base): # Tausers라는 테이블을 class화 시켰음, 함수들은 sqlachemy에서 지원하는 함수들 사용(Column, Integer ...)
    __tablename__ = "tauser"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email =  Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    Base = declarative_base()

class Crawling(Base): # crawling라는 테이블을 class화 시켰음, 함수들은 sqlachemy에서 지원하는 함수들 사용(Column, Integer ...)
    __tablename__ = "crawling"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email =  Column(String)
    itemname =  Column(String)
    price = Column(Integer)
    link = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    Base = declarative_base()

# CRUD 실행
class MySQLDatabase:
    def __init__(self, db_url): # db와 연동
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        # Base.metadata.create_all(self.engine)
    # create
    def add_user(self, username, email): # 
        session = self.Session()
        user = Tausers(username=username, email=email)
        session.add(user)
        session.commit()
        session.close()
    # read
    def get_user_by_username(self, username):
        session = self.Session()
        user = session.query(Tausers).filter_by(username=username).first()
        session.close()
        return user

    def get_user_by_email(self, email):
        session = self.Session()
        user = session.query(Tausers).filter_by(email=email).first()
        session.close()
        return user
    # update
    def update_user_email(self, username, new_email):
        session = self.Session()
        user = session.query(Tausers).filter_by(username=username).first()
        if user:
            user.email = new_email
            session.commit()
        session.close()
    # delete
    def delete_user(self, username):
        session = self.Session()
        user = session.query(Tausers).filter_by(username=username).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()

    # file to sql 연동
    def to_sql(self):
        df = pd.read_excel(r"C:\Users\hojun\Downloads\workspace01\data\모자결과물.xlsx")
        try:
            df.to_sql(name="crawling",con=self.engine)
            print("로그 남김 성공")
            # to_do : 로그기록 남기기
        except Exception as e:
            print(e)

# main이면 해당 계정으로 연결을 시도해라 >> 프로젝트에선 runner.py에서 실행되어야
# if __name__ == "__main__":
#     try:
#         user = "root"
#         password = ""
#         host = "localhost"
#         port = 3306
#         db = "test"

#         db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
#         db = MySQLDatabase(db_url)

#         print(db.__repr__)
    
#         db.add_user("john_doe", "john@example.com")
#         user =  db.get_user_by_username("john_doe")
#         #print(user.username, user.email)
#         db.update_user_email("john_doe", "new_email@example.com")
#         user =  db.get_user_by_username("john_doe")
#         # print(user.username, user.email)

#         # db.delete_user("john_doe")

#     except Exception as e:
#         print("DB부분처리안됨")    
#         print("e")