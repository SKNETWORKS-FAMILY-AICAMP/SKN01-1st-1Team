import PySimpleGUI as sg
import os.path

# 클래스화 하기

class Mainv:
    def __init__(self):
        left_col = [
            [sg.Text("이미지가 들어있는 폴더를 선택해주세요."),
             # enable_events : 변경이 있을 때 반영하겠다?의 의미
             # key : 
             sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
             sg.FolderBrowse(button_text="열기")], # []안에 있는 []의 내용을 길게할수록 --> 로 나열 됨
            # listbox 넣기
            [sg.Listbox(values=[], enable_events=True, size=(40,20), key="-FILE LIST-")],
        ]

        image_col = [
            [sg.Text("선택한 폴더의 이미지 리스트")],
            [sg.Text(size=(40,1), key="-TOUT-")],
            [sg.Image(key="-IMAGE-")],
        ]

        layout = [
            sg.Column(left_col),
            sg.VSeperator(),
            sg.Column(image_col)
        ],

        window = sg.Window("이미지뷰어", layout)

        while True:
            event, values = window.read() # read 올려보면 tuple형식으로 반환함을 확인할 수 있음 그러므로 받아줄 event, value 2개

            if event in (None, "Exit"): # 반환된게 없거나, Exit 버튼을 눌렀다면 종료하기
                break
            if event == "-FOLDER-":
                folder = values["-FOLDER-"] # FOLDER에 대한 경로주소 문자열이(values에 의해) folder에 들어감
                try:
                    file_list = os.listdir(folder) #  listdir로 인한 (파일명)을 list로 반환
                    # print(file_list)
                except Exception as e: # 그냥 except하지말고 Exception as e 를 습관적으로 어떤 에러인지 확인하기 위함
                    print(e)
                    file_list = [] # 제대로 안담겼다면, file_list를 빈 list로 만듦

                # 파일 이름만들기 (핵심 부분)
                fnames = [
                    # list comprehension []안에 for, if, append가 실행됨
                    f
                    for f in file_list
                    if os.path.isfile(
                        os.path.join(folder, f) # 풀 경로만들어주기 
                    ) and f.lower().endswith((".png",".jpg",".jpeg",".tiff",".bmp")) # endswith() 끝부분을 확인하는 함수 >> 파일명 끝부분이 소문자냐?
                ]

                # listbox에 FILE LIST 선언했음 >> listbox는 파일경로 
                window["-FILE LIST-"].update(fnames)
            
            elif event == "-FILE LIST-":
                try:
                    filename = os.path.join(values["-FOLDER-"],values["-FILE LIST"][0]) # (풀경로, 파일명) 2개를 연결해줘
                    window["-TOUT-"].update(filename) # 윈도우에 가져온 filename update
                    window["-IMAGE-"].update(filename=filename) # 키워드인자 = filename
                except Exception as e:
                    # print(e)
                    pass

        window.close()