# 개별 학생의 정보를 추출하는 클래스

class getstudent():
    def __init__(self, name, kor, eng, math, sci):
        self.name=     name  
        self.kor=      kor
        self.eng=      eng
        self.math=     math
        self.sci=      sci

    def get_student_info(self):
        print(f"{self.name},{self.kor},{self.eng},{self.math},{self.sci}")

    def sum(self):
        sum = self.kor + self.math + self.sci + self.eng
        return sum
    def average(self):
        avg = (self.kor + self.math + self.sci + self.eng) / 4
    def to_string(self):
        result = f"{self.name}학생의 성적총합은 {self.sum()} 평균은 {self.average()}"