import pandas as pd
import pymysql.cursors
from sqlalchemy import engine, create_engine, DateTime, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
import sqlalchemy
# from sqlalchemy.orm import declarative_base

# 자동화로 만들어야할 것 같음, 테이블마다 입력 직접 지정하기 어려움
def record_insert(file_path, db_url, table):
    df = pd.read_excel(file_path)
    
    # table insert 방법 1 (너무 일일이 설정해야함)
    # connection = pymysql.connect(host='localhost', user='root', password='', db='project')
    # for i in range(len(df)):
    #     model = df["모델명"][i]
    #     price = df["가격"][i] # 난 그냥 db table varchar로 해서 해결
    #     old = df["연식"][i]
    #     distance = df["주행 거리"][i]
    #     energy = df["연료"][i]
    #     location = df["거래 장소"][i]

    #     with connection.cursor() as cursor:
    #         # test db의 crawlilng table에 해당 정보 입력
    #         #cursor.execute("INSERT INTO crawling (itemname, price, link) VALUES ('{}','{}','{}')".format(상품명, 가격, 링크))
    #         cursor.execute("INSERT INTO crawling (model, price, old, distance, energy, location) \
    #                     VALUES ('{}','{}','{}','{}','{}','{}')".format(model, price, old, distance, energy, location))
    #         connection.commit()

    # table insert 방법 2 (1번 방법보단 자동화)
    db_conn = create_engine(db_url) # 보낸 db_url과 db연동 (db_url : 계정 정보와 연결할 db명이 담겨있음)
    # id는 알아서 들어가져 있음
    # table마다 맞게 데이터타입 설정은 해야 함 >> pd로 자동화 가능함 (각 column 뽑고, 맞는 데이터타입은 전부 string으로..)
    #print(df.columns[1:][1]) # dataframe의 모든 column
    
    # table column : 여긴 알아서 바꾸기! 
    dtypesql = {'title':sqlalchemy.types.VARCHAR(30), 
        'review':sqlalchemy.types.VARCHAR(200), 
        'model':sqlalchemy.types.VARCHAR(20), 
        'date':sqlalchemy.DateTime(),
        }
    # # 이미 테이블이 있다면 append한다.
    df.to_sql(name=table, con=db_conn, if_exists='append', index=False, dtype=dtypesql)

Base = declarative_base() # 실제 테이블에 선언되어 있는 방식으로 받아들이겠다.

class crawling(Base): # crawing라는 테이블을 class화 시켰음,    함수들은 sqlachemy에서 지원하는 함수들 사용(Column, Integer ...)
    __tablename__ = "crawling"
    id = Column(Integer, primary_key=True)
    model = Column(String)
    price =  Column(String)
    old = Column(String)
    distance = Column(String)
    energy = Column(String)
    location = Column(String)



# CRUD 기능 넣기 by alchemy
class MySQLDatabase:
    def __init__(self, db_url): # db와 연동
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    # create
    def add_user(self, carid): # 
        session = self.Session()
        car = crawling(carid=carid)
        session.add(car)
        session.commit()
        session.close()
    # read
    def get_user_by_carid(self, carid):
        session = self.Session()
        user = session.query(crawling).filter_by(carid=carid).first()
        session.close()
        return user

    def get_user_by_email(self, email):
        session = self.Session()
        user = session.query(crawling).filter_by(email=email).first()
        session.close()
        return user
    # update
    def update_user_email(self, username, new_email):
        session = self.Session()
        user = session.query(crawling).filter_by(username=username).first()
        if user:
            user.email = new_email
            session.commit()
        session.close()
    # delete
    def delete_user(self, username):
        session = self.Session()
        user = session.query(crawling).filter_by(username=username).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()