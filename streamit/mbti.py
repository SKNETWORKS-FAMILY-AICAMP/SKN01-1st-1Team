import json
import configparser # 중요! ini 파일 뜯어낼 때 주로 사용 >> 나중에 클래스만들어놓고 필요한기능 가져다쓰면 됨
# json, toml, yaml, xml 알아두는게 좋음

import http.client
import streamlit as st

class CompletionExecutor:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def _send_request(self, completion_request):
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id
        }

        conn = http.client.HTTPSConnection(self._host)
        # dump : 문자열화 시킨다.
        conn.request('POST', '/testapp/v1/completions/LK-D', json.dumps(completion_request), headers)
        response = conn.getresponse()
        result = json.loads(response.read().decode(encoding='utf-8'))
        conn.close()
        return result

    def execute(self, completion_request):
        res = self._send_request(completion_request)
        if res['status']['code'] == '200': # error 종류 404, 등..
            return res['result']['text']
        else:
            return 'Error'

# configparse 만드는 부분 해보면 좋음!
config = configparser.ConfigParser()
config.sections()
config.read('./your_apikey.ini') # 코드에 담지말고 바깥으로 빼서 

# 나중에 chat ai에 활용하면 좋을 듯
completion_executor = CompletionExecutor(
    host=config['CLOVA']['host'],
    api_key=config['CLOVA']['api_key'],
    api_key_primary_val=config['CLOVA']['api_key_primary_val'],
    request_id=config['CLOVA']['request_id']
)

st.title('MBTI 대백과사전')
question = st.text_input(
    '질문', 
    placeholder='질문을 입력해 주세요'
)

if question:
    preset_text = f'MBTI에 대한 지식을 기반으로, 아래의 질문에 답해보세요.\n\n질문:{question}'

    request_data = {
        'text': preset_text,
        'maxTokens': 100,
        'temperature': 0.5,
        'topK': 0,
        'topP': 0.8,
        'repeatPenalty': 5.0,
        'start': '\n$$$답:',
        'stopBefore': ['###', '질문:', '답:', '###\n'],
        'includeTokens': True,
        'includeAiFilters': True,
        'includeProbs': True
    }

    response_text = completion_executor.execute(request_data)
    st.markdown(response_text.split('$$$')[1])