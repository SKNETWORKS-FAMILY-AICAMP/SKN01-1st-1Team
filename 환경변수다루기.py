import os # 환경변수 관련 세팅

# print(os.environ)
# print(os.getenv("path")) # getenv(key)

os.environ["PATH"] = r"C:\laragon\bin\mysql\mysql-8.0.30-winx64\bin"
print(os.getenv("path"))