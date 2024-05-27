from flask import Flask
import os

# 파이썬이 이 파일을 직접실행시키면 이 파일의 __name__은 __main__이 됨
# if "__name__" == "__main__":

# class instance 만들기
app = Flask(__name__)
# print(dir(app))

# python에서 @역할 : decorator >> 함수를 감싸줘서 기능을 추가해 준다. (함수를 변경하는 것 >> 오버로딩?)
# 미리 만들어둔 데코레이터
# 내가 만들어쓰는 데코레이터 (기존 기능에 추가)
# 근데 여기서 사용된 @는 파이썬 자체의 데코레이터가 아닌 flask의 데코레이터

# route : 라우터 기능 >> 경로를 추가 (처리)
@app.route("/") # 웹 주소의 루트 경로

def hello():
    return "<h1>Hello World!</h1>"

# localhost = 127.0.0.1

# 파이썬 자체에 내장된 서버 : http.server