# import test_module as test # test_module.py 불러오기
# # c++의 header file과 main file의 느낌

# # module의 함수들 다 불러옴 number_input, get_circumference, get_circle_area
# radius = test.number_input()
# print(test.get_circumference(radius))
# print(test.get_circle_area(radius))


# 446 page (하부 패키지 test_package에 있는 파일 불러오기)
# from test_package import module_a as a, module_b as b

# print(a.varialbe_a)
# print(b.variable_b)

# init으로 초기화 설정한 이후 import없이 부르기 (448 page)
# from test_package import *

# if __name__ == "__main__":
#     print(module_a.varialbe_a)
#     print(module_b.variable_b)

# 455 page 실습 : 인터넷 이미지 불러오기
from urllib import request

target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
# target = open("1024.png","r") # 위와 동치? (읽기모드로 열기)
# with open("1024.png","r") as read_file:
#     output = read_file.read()

output = target.read() # 읽기모드 상태

# 읽기모드를 바꾸기 > 편집할거면 쓰기모드로 바꿔야
file = open("output.png", mode="wb") # 해당모드로 바꿔서 이미지 내보내기
file.write(output)
# with open("output.png","w") as file:
#     file.write(output)


file.close()
