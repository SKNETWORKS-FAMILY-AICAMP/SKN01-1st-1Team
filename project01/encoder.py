import base64
import sys


print("encoder 로드되고 실행된 name",__name__) # encoder를 불러올때 __name__ 출력하도록

def str_to_base64(x):
    """문자열을 base64 표현으로 변환함

    b64encode()는 bytes-like objec를 인수로 받으므로
    문자열은 encode()로 bytes 타입으로 전달함
    """
    return base64.b64encode(x.encode('utf-8'))


def main():
    # python3 encoder.py book 으로 명령어 실행하면
    # argument value : argv
    전체 = sys.argv # list 형식
    실행파일명 = sys.argv[0] # python이 직접 실행시킨 파일 첫번째인자 encoder.py 이 들어옴
    옵션 = sys.argv[1] # python이 직접 실행시킨 파일 두번째인자 book이 들어옴
    print(str_to_base64(옵션))
    print("전체", 전체)


# 파이썬에서 직접 실행시킨 시작파일 python main.py 역할
if __name__ == '__main__':
    main()

