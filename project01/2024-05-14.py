# beautifulsoup4 사용
from bs4 import BeautifulSoup # beautifulsoup class 사용
from urllib import request # request module
from flask import Flask

# 웹서버 생성
app = Flask(__name__)
@app.route("/")

def get_url():
    # 가져올 웹페이지 > 기상청 사이트로해서 기상청의 전국날씨 읽기
    # target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnID=108")
    # target : byte 문자열
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnID=108")
    
    # BeautifulSoup을 통해 웹페이지 분석
    soup = BeautifulSoup(target, "html.parser")

    # location 태그를 찾기
    output = ""
    for loc in soup.select("location"):
        # print(f"도시: {item.select_one('city').string}")
        output += "<h3>{}</h3>".format(loc.select_one("city").string)
        output += "날씨 : {}<br/>".format(loc.select_one("wf").string)
        output += "최저/최고 기온: {}/{}"\
            .format(\
                loc.select_one("tmn").string,\
                loc.select_one("tmx").string\
                )
        output += "<hr/>"
    return output
