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
        CREATE TABLE IF NOT EXISTS review (
            id INT AUTO_INCREMENT PRIMARY KEY,
            제목 TEXT,
            내용 TEXT,
            차종 TEXT,
            리뷰날짜 TEXT
        );
    """
    cursor.execute(create_table_query)
    print("Table 'review' created successfully.")


def insert_data_from_xlsx(cursor, file_path):
    # XLSX 파일에서 데이터를 읽어옴
    data = pd.read_excel(file_path)

    # 데이터를 데이터베이스에 삽입
    for index, row in data.iterrows():
        제목 = row["제목"]
        내용 = row["내용"]
        차종 = row["차종"]
        리뷰날짜 = row["리뷰 날짜"]

        cursor.execute(
            "INSERT INTO review (제목, 내용, 차종, 리뷰날짜) VALUES (%s, %s, %s, %s);",
            (제목, 내용, 차종, 리뷰날짜),
        )

    print("Data inserted into the database successfully.")


if __name__ == "__main__":
    # MySQL 연결 정보
    host = "localhost"
    user = "encore"
    password = "encore1234"
    db_name = "used_car"
    file_path = r"C:\Users\USER\Dropbox\BOOTCAMP\workspace\1st_project\data\review.xlsx"

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
