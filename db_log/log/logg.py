import os
import logging

class Logger:
    def __init__(self, file):
        self.logger = logging.getLogger("파일로그")
        # 보지 않을 때에도 로그기록을 확인하기 위해 파일로 남김
        self.file_name = os.path.basename(file)

        # 로그가 생성이 안 되었다면
        if len(self.logger.handlers) == 0:
            formatter = logging.Formatter(u'%(asctime)s [%(levelname)s] %(message)s')
            stream_handler = logging.FileHandler(self.file_name, encoding="utf-8") # handler 객체 생성, 한글 깨지니 utf-8로
            stream_handler.setFormatter(formatter) # 입력한 포맷(formatter)에 맞게 로그를 남기겠다.

            self.logger.addHandler(stream_handler) # 이걸 해야 로그 기록시작
            self.logger.setLevel(logging.INFO) # 다 볼 필요는 없으니, 어느 정도만 보여줄건지 설정 >> 보통 INFO를 찍음
    
    def info(self, value):
        # f-string외에 다른 방식, 흰색 % 기준으로 각 %s에 변수들이 대응됨
        self.logger.info("%s (at %s)" % (str(value), self.file_name))
    
    def error(self, value):
        self.logger.error("%s (at %s)" % (str(value), self.file_name))