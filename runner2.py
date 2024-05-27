from helpers.crawling2 import User
import pandas as pd
import time


if __name__ == "__main__":

    user = User("n")
    user.페이지이동("https://www.kcar.com/cs/csQstn")

    user.일반딜레이(3)

    질문 = []
    답변 = []

    내차사기 = 18
    내차팔기 = 12
    회원정보관리 = 3
    금융 = 2
    렌트 = 24
    보증서비스 = 6
    기타 = 5
    # 낭ㄹㄴㄹㄴㅇ
    xpath = [18, 12, 3, 2, 24, 6, 5]

    for i in range(0, 7):
        try:
            user.객체선택하고클릭(
                f"/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div[{i+2}]"
            )
            user.일반딜레이(3)
            for j in range(0, xpath[i]):
                try:
                    질문.append(
                        user.객체선택하고객체의텍스트추출(
                            f"/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[{i+1}]/div/div/div[{j+1}]/div[1]/div/span"
                        )
                    )
                    user.일반딜레이(3)
                except Exception as e:
                    질문.append("질문안들어옴")
                    print(f"{i}페이지{j}질문 오류")
                user.객체선택하고클릭(
                    f"/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[{i+1}]/div/div/div[{j+1}]/div[1]/div/span"
                )
                user.일반딜레이(3)
                try:
                    답변.append(
                        user.객체선택하고객체의텍스트추출(
                            f"/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[{i+1}]/div/div/div[{j+1}]/div[2]/div/div/div"
                        )
                    )
                    user.일반딜레이(3)
                except Exception as e:
                    답변.append("답변안들어옴")
                    print(f"{i}페이지{j}질문 오류")

        except Exception as e:
            print(e)
    df = pd.DataFrame(data=zip(질문, 답변), columns=["질문", "답변"])
    df.to_excel(r"C:\Users\USER\Dropbox\BOOTCAMP\workspace\1st_project\data\FAQ1.xlsx")

    time.sleep(3)
