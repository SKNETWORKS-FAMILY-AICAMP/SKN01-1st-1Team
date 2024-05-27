# 파이썬과 데이터 베이스 연동
import pymysql
import pymysql.cursors

# host, user, pw, 어떤 db를 볼지
conn = pymysql.connect(host="localhost", user="encore", passwd="encore1234") 

# 커서 객체 생성 (쿼리를 실행하기 위한 것)
cur = conn.cursor(pymysql.cursors.DictCursor)

# with문으로 file open하기
with open(r"C:\Users\hojun\Downloads\employees\employees.sql", encoding="utf-8") as file:
    sql = file.read() # 파일 읽어들이기
sql = sql.split(";") # ; 단위로 쪼개기 -> 리스트로 담음

# 쿼리 날리기
for i in sql:
    try:
        print(cur.execute(i))
    except Exception as e:
        print(e)
        # i.replace("/","\\") # / 를 \로 바꿔준다. 근데 이렇게 하지말고 os.path를 이용해주는게 좋음
        import os
        print(os.path.sep)
        i.replace("\\",os.path.sep) # /를 os.path.sep (seperator) 에 맞게 >> 근데 escaping 고려해야해서 //로 ?

# result = cur.fetchall() # 쿼리에 해당하는 데이터들 출력 [{}, {} ...] list안에 dict들
# # print(result[0]["to_date"]) # 첫번째 dict에 to_data란 키 가져오기 
# print(result)


