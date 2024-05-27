from student.getdata import jsonplaceholder
from student.getstudent import getstudent

if __name__ == "__main__":
    # student = jsonplaceholder()
    # print(student[0]["name"]) # index 뿐만 아니라 키 값("name")으로도 접근 가능
    # print("id","name","username","email")
    # for st in student:
    #     print(f"{st["id"]}{st["name"]} \ 
    #           {st["username"]}{st["email"]}")
    
    s1 = getstudent('hj',50,50,50,50)
    s1.get_student_info()

    s1.math

# set comprehension
# set for (if) : for문을 돌며 조건문 있다면 수행하고 나온 결과를 set로 반환
# {set for (if)}

# dict comprehension
# a = { f"{key}" : item for item in range(0,10)} , key를 str로 넣을거면 이렇게 아니라면 그냥 idx활용