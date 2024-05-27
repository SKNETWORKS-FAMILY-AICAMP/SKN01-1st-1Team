import pymysql
import pandas as pd


def create_database(cursor, db_name):
    # 데이터베이스 생성 SQL 쿼리
    create_db_query = f"CREATE DATABASE IF NOT EXISTS {db_name};"
    cursor.execute(create_db_query)
    print(f"Database '{db_name}' created successfully.")


def create_table(cursor):
    # 테이블 생성 SQL 쿼리
    create_table_query = """
        CREATE TABLE IF NOT EXISTS carlist (
            id INT AUTO_INCREMENT PRIMARY KEY,
            모델명 TEXT,
            가격 TEXT,
            연식 TEXT,
            주행거리 TEXT,
            연료 TEXT,
            거래장소 TEXT
        );
    """
    cursor.execute(create_table_query)
    print("Table 'carlist' created successfully.")


def insert_data_from_xlsx(cursor, file_path):
    # XLSX 파일에서 데이터를 읽어옴
    data = pd.read_excel(file_path)

    # 데이터를 데이터베이스에 삽입
    for index, row in data.iterrows():
        모델명 = row["모델명"]
        가격 = row["가격"]
        연식 = row["연식"]
        주행거리 = row["주행 거리"]
        연료 = row["연료"]
        거래장소 = row["거래 장소"]

        cursor.execute(
            "INSERT INTO carlist (모델명, 가격, 연식, 주행거리, 연료, 거래장소) VALUES (%s, %s, %s, %s, %s, %s);",
            (모델명, 가격, 연식, 주행거리, 연료, 거래장소),
        )

    print("Data inserted into the database successfully.")


if __name__ == "__main__":
    # MySQL 연결 정보
    host = "localhost"
    user = "encore"
    password = "encore1234"
    db_name = "used_car"
    file_path = r"C:\Users\USER\Dropbox\BOOTCAMP\workspace\1st_project\data\K-car.xlsx"

    # MySQL 연결
    connection = pymysql.connect(host=host, user=user, password=password)
    cursor = connection.cursor()

    # 데이터베이스 생성
    create_database(cursor, db_name)

    # 생성한 데이터베이스에 연결
    cursor.execute(f"USE {db_name};")

    # 테이블 생성
    create_table(cursor)

    # 데이터 삽입
    insert_data_from_xlsx(cursor, file_path)

    # 변경 사항 저장 및 연결 종료
    connection.commit()
    connection.close()