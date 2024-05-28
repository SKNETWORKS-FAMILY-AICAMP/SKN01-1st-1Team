from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import subprocess
from urllib.parse import quote_plus
import os
import signal
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_driver = r"C:\Users\USER\Desktop\workspace01\crawling\driver\chromedriver.exe"


# self.chrome_options.add_argument("--headless")  # Head-less 설정
# self.chrome_options.add_argument("--no-sandbox")
# self.chrome_options.add_argument("--disable-dev-shm-usage")
class User:
    def __init__(self, mode="n"):
        # 작동시작로그
        # 새브라우저를 컨트롤할건지
        self.chrome_driver = chrome_driver
        self.chrome_options = Options()
        if mode == "n":
            self.browser = webdriver.Chrome(options=self.chrome_options)
        # else:
        #     # 작동중인 브라우저를 컨트롤할건지
        #     # debugging 모드와 9222 포트로 실행시킨 Chrome에 접근
        #     # chrome://version/
        #     # 수동으로 브라우저 작동시키기
        #     # subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
        #     # C:\Users\user> cd C:\Program Files\Google\Chrome\Application
        #     # C:\Program Files\Google\Chrome\Application> chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeTEMP"
        #     # Change chrome driver path accordingly
        #     cmd = [
        #         "C:\Program Files\Google\Chrome\Application\chrome.exe",
        #         "--remote-debugging-port=9222",
        #         '--user-data-dir="C:\ChromeTEMP"',
        #     ]
        #     # The os.setsid() is passed in the argument preexec_fn so
        #     # it's run after the fork() and before  exec() to run the shell.
        #     pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        #     pro.kill()

        #     # os.killpg(os.getpgid(pro.pid), signal.SIGTERM)  # Send the signal to all the process groups
        #     self.chrome_options.add_experimental_option(
        #         "debuggerAddress", "127.0.0.1:9222"
        #     )
        #     self.browser = webdriver.Chrome(options=self.chrome_options)
        self.browser.maximize_window()
        print("브라우저작동됨")

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def 페이지이동(self, page):
        self.browser.get(page)

    def 객체선택(self, user_xpath):
        return self.browser.find_element(By.XPATH, user_xpath)

    def 객체선택값입히고(self, user_xpath, item_name):
        self.browser.find_element(By.XPATH, user_xpath).send_keys(item_name)

    def 객체선택하고클릭(self, user_xpath):
        try:    
            self.browser.find_element(By.XPATH, user_xpath).click()
        except:
            clickable = self.browser.find_element(By.XPATH, user_xpath)
            action = ActionChains(self.browser).move_to_element(clickable)
            action.perform()
            clickable.click()
        # self.browser.find_element(By.XPATH, user_xpath).send_keys(Keys.ENTER)
    def 객체선택하고객체의텍스트추출(self, user_xpath):
        return self.browser.find_element(By.XPATH, user_xpath).text

    def 종료(self):
        self.browser.close()
        print("작업완료됨로그찍기")

    def 브라우저딜레이(self, second=1):
        #self.browser.implicitly_wait(second)
        time.sleep(second)

    def 일반딜레이(self, second=1):
        time.sleep(second)

    def 새창으로활성이동(self, idx):
        # window_handles[0...]
        print(self.browser.window_handles)  # 0
        # 셀레늄이 바라보는 윈도우를 변경할 때는 switch_to 메서드를 사용합니다.
        self.browser.switch_to.window(self.browser.window_handles[idx])

    def 마우스이동하고클릭(self, user_xpath):
        ac = ActionChains(self.browser)
        # ac.move_by_offset(0, 350)
        # ac.click()
        web_elements = self.browser.find_element(By.XPATH, user_xpath)
        ac.click(web_elements)
        ac.perform()

    def 페이징(self, user_full_xpath):
        self.browser.find_element(By.XPATH, user_full_xpath).click()
