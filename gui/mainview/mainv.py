import PySimpleGUI as sg
import os.path
from glob import glob # 원래는 외부 라이브러리나, 다른거 설치하면서 의존성으로 같이 설치된듯

class Mainv:
    def __init__(self):
        left_col = [
            [
                sg.Text("이미지가 들어있는 폴더를 선택해주세요"),
                sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
                sg.FolderBrowse(button_text="열기"),
            ],
            [
                sg.Listbox(
                    values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
                )
            ],
        ]

        image_col = [
            [sg.Text("선택한 폴더의 이미지 리스트")],
            [sg.Text(size=(40, 1), key="-TOUT-")],
            [sg.Image(key="-IMAGE-")],
        ]
        
        # 윈도우에 메뉴창 추가하고 싶으면 layout 쪽 다루기 
        layout = [
            [sg.Menu([["메뉴"], ["파일"]])],
            [sg.Column(left_col), sg.VSeparator(), sg.Column(image_col)]
            ]

        window = sg.Window("이미지뷰어", layout)
        #window.finalize() # maximize() 하기전에 finalize 해줘야 오류 x
        #window.maximize() # 윈도우창 최대화

        while True:
            event, values = window.read()

            if event in (None, "Exit"):
                break
            if event == "-FOLDER-":
                folder = values["-FOLDER-"]
                try:
                    file_list = os.listdir(folder)
                    # print(file_list)
                except Exception as e:
                    print(e)
                    file_list = []
                
                # file 다루기 기존 방법 1
                # fnames = [
                #     f
                #     for f in file_list
                #     if os.path.isfile(os.path.join(folder, f))
                #     and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp"))
                # ]

                # file 다루는 2번째 방법 glob
                # 리스트업 table
                # 최대화
                fnames = glob(r"C:\Users\hojun\Downloads\수업공유폴더\**\*.png", recursive=True) # 모든 하위폴더의 png파일 탐색
                print(fnames)

                fnames = glob(folder)

                window["-FILE LIST-"].update(fnames)
            # 테이블객체로 리스트업
            elif event == "-FILE LIST-":
                try:
                    filename = os.path.join(
                        values["-FOLDER-"], values["-FILE LIST-"][0]
                    )
                    window["-TOUT-"].update(filename)
                    window["-IMAGE-"].update(filename=filename)
                except Exception as e:
                    print(e)
                    pass

        window.close()