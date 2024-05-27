# 셀레니움할땐 뭔가 많이 가져와야함
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import subprocess # command 부르는 용도
from urllib.parse import quote_plus
import os

# 크롤링을 돌리는 클래스 만들기
chrome_driver = r"C:\Users\hojun\Downloads\workspace01\driver\chromedriver.exe"

class User:
    # init시에는 크롬이 올라오도록 설정하기
    def __init__(self, mode="n"):
        # 작동시작 로그남기기

        # 터미널에서 수동으로 브라우저 작동시키기
        # cd C:\Program Files\Google\Chrome\Application
        # chrome.exe --remote-debugging-port=9222--user-data-dir="C:\ChromeTEMP”
        
        # vscode에서 브라우저 작동시키기
        self.chrome_options = Options()
        # 방법 1. 새 브라우저를 컨트롤 할지 (로그인, 확장기능이 되어있는 것)
        if mode == "n":
            # 브라우저를 통해 제어
            self.browser = webdriver.Chrome(options=self.chrome_options)
            self.browser.maximize_window()

        # 방법 2. 기존 브라우저를 컨트롤 할지 (로그인x, 확장기능 없는 초기 브라우저)
        # 디버그 모드로 실행시키고 version 정보 맞추기      
        # 옵션 설정 >> 현재 옵션엔 기본 제외 아무것도 안 넣음 (새 브라우저 상태)
        else:
            # subprocess.call(
            #     [
            #         'C:\Program Files\Google\Chrome\Application\chrome.exe', 
            #         '--remote-debugging-port=9222',
            #         '--user-data-dir="C:\ChromeTEMP"']
            # )
            cmd = [
                    'C:\Program Files\Google\Chrome\Application\chrome.exe', 
                    '--remote-debugging-port=9222',
                    '--user-data-dir="C:\ChromeTEMP"']
            pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
            
            self.options.add_experimental_option("debuggerAddress", "127.0.0.1:9222") # 뭐에대한 주소? >> 나의 포트번호!
            self.browser = webdriver.Chrome(options=self.chrome_options)

    def 페이지이동(self, page):
        self.browser.get(page)

    def 객체선택값입히기(self, user_xpath, item_name):
        self.browser.find_element(By.XPATH, user_xpath).send_keys(item_name) # xpath 방식으로 element 찾겠다.

    def 객체선택하고클릭(self, user_xpath):
        self.browser.find_element(By.XPATH, user_xpath).click() # 클릭 기능 구현

    def click_button(self,button_xpath):
        try:
            #self.browser.find_element(By.XPATH, button_xpath).click()
            self.browser.find_element(By.XPATH, button_xpath).send_keys(Keys.ENTER)
            #ActionChains(self.browser).click(clickable).perform()
            print('버튼 클릭 성공')
        except Exception as e:
            print('By.XPATH로 클릭되지 않습니다. By.PARTIAL_LINK_TEXT로 접근합니다! ')
            time.sleep(1) # 딜레이를 충분히 줘야 에러가 안 남
            try:
                totext = self.find_ele_text(button_xpath) # 버튼 이름 텍스트로 가져와서
                self.browser.find_element(By.PARTIAL_LINK_TEXT, totext).click() # By.PARTIAL_LINK_TEXT 안에 넣어줌

                print('성공!')
                if totext == None: # 텍스트 받아오기를 실패하면 직접 이름 입력
                    print('해당 버튼의 키워드(이름)를 추가로 입력하세요. --> click_button(XPATH, 버튼 이름)')
                    
            except Exception as e:
                print('문제발생!', type(e))

    # 해당 XPATH의 요소의 text 반환하는 함수
    def find_ele_text(self,user_xpath):
        text = self.browser.find_element(By.XPATH, user_xpath).text.strip()
        return text

    def paging(self, user_path):
        #return self.browser.find_elements(By.CSS_SELECTOR,'#app > div.searchWrap > div.containerWrap.cSection.el-row > div.kcarSearchCnt > div:nth-child(4) > div:nth-child(2) > div.pagination.-sm > div')
        #app > div.searchWrap > div.containerWrap.cSection.el-row > div.kcarSearchCnt > div:nth-child(4) > div:nth-child(2) > div.carListWrap
        time.sleep(1)
        return self.browser.find_element(By.XPATH, user_path).text


    # 선택한값 클릭하진 말고 텍스트로 반환만
    def 객체선택(self, user_xpath):
        return self.browser.find_element(By.XPATH, user_xpath).text
    
    def 종료(self):
        print("종료된 로그 찍기")
        self.browser.close()
    
    # delay 기능 넣기
    def delay(self, sec=1):
        self.browser.implicitly_wait(sec)
        

    def 새창으로활성이동(self, number):
        # 셀레니움은 윈도우 구분을 위해 window_handles 변수에 이름을 리스트로 저장
        # 리스트에는 윈도우가 생성된 순으로 저장됨
        print(self.browser.window_handles) # 팝업된 윈도우들 몇개있나 보여주기
        self.browser.switch_to.window(self.browser.window_handles[number]) # 기존 객체에서 1번 객체(윈도우)로 이동 by 'switch_to'
    
    def 마우스이동하고클릭(self, user_xpath):
        ac = ActionChains(self.browser)
        # ac.move_by_offset(0, 350)
        web_elements = self.browser.find_element(By.XPATH, user_xpath)
        ac.click(web_elements)
        # ac.click()
        ac.perform()
    
    # 페이지 넘어가는 규칙에 따라 넘어가기 실행
    def paging(self, user_full_xpath):
        self.browser.find_element(By.XPATH, user_full_xpath)