from helpers.crawlingsele import User
import pandas as pd
import time, os

if __name__ == "__main__":

    user = User("n")
    user.페이지이동("https://www.kcar.com/cs/csQstn")

    time.sleep(3)

    질문 = []
    답변 = []

    # 각 태그별 질문 개수
    xpath = [18, 12, 3, 2, 24, 6, 5]

    for i in range(0, 7):
        try:
            user.객체선택하고클릭(f'/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div/div[{i+2}]')
            time.sleep(1)
            for j in range(0, xpath[i]):
                try:
                    질문.append(
                        user.객체선택(
                            f"/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[{i+1}]/div/div/div[{j+1}]/div[1]/div/span"
                        )
                    )
                    time.sleep(1)
                except Exception as e:
                    질문.append("질문안들어옴")
                    print(f"{i}페이지{j}질문 오류")
                user.객체선택하고클릭(
                    f"/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[{i+1}]/div/div/div[{j+1}]/div[1]/div/span"
                )
                time.sleep(1)
                try:
                    답변.append(
                        user.객체선택(
                            f"/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[1]/div[2]/div[{i+1}]/div/div/div[{j+1}]/div[2]/div/div/div"
                        )
                    )
                    time.sleep(1)
                except Exception as e:
                    답변.append("답변안들어옴")
                    print(f"{i}페이지{j}질문 오류")
        except Exception as e:
            print(e)
    df = pd.DataFrame(
        data=zip(질문, 답변),
        columns=["질문", "답변"]
    )
    # os.getcwd()로 경로 맞춤
    df.to_excel(os.getcwd() + "\\data\\FAQ.xlsx", index=False)