# 디비로 저장한다. => 수집 될 때 마다 한다.
# sql알케미 db연동 코드 참고
# 크롤링은 수집한 데이터를 db에 잘 저장하는것이 매우 중요 >> 이 부분 잘 알아두기!

from sqlalchemy import engine, create_engine, DateTime, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base() # 실제 테이블에 선언되어 있는 방식으로 받아들이겠다.

class Tausers(Base): # Tausers라는 테이블을 class화 시켰음, 함수들은 sqlachemy에서 지원하는 함수들 사용(Column, Integer ...)
    __tablename__ = "tauser"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email =  Column(String)
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

# main이면 해당 계정으로 연결을 시도해라
if __name__ == "__main__":
    try:
        user = "root"
        password = ""
        host = "localhost"
        port = 3306
        db = "test"

        db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        db = MySQLDatabase(db_url)

        # 변수 = eval(변수) : eval 기능 객체화시켜줌 >> 보안적으로 문제가 되어 사용 권장은 x
        # 이걸 활용하면 동적 변수로서 사용가능 하지만  __repr__ 을 활용하자
        print(db.__repr__)
    
        db.add_user("john_doe", "john@example.com")
        user =  db.get_user_by_username("john_doe")
        #print(user.username, user.email)
        db.update_user_email("john_doe", "new_email@example.com")
        user =  db.get_user_by_username("john_doe")
        # print(user.username, user.email)

        # db.delete_user("john_doe")

    except Exception as e:
        print("DB부분처리안됨")    
        print("e")


# 디비명 test

# CREATE TABLE `tauser` (
#   `id` INT(10) NOT NULL AUTO_INCREMENT,
#   `username` VARCHAR(50) NOT NULL DEFAULT '0' COLLATE 'utf8mb4_general_ci',
#   `email` VARCHAR(50) NOT NULL DEFAULT '0' COLLATE 'utf8mb4_general_ci',
#   `created_at` TIMESTAMP NULL DEFAULT NULL,
#   `updated_at` TIMESTAMP NULL DEFAULT NULL,
#   PRIMARY KEY (`id`) USING BTREE
# )
# COLLATE='utf8mb4_general_ci'
# ENGINE=InnoDB
# AUTO_INCREMENT=5
# ;