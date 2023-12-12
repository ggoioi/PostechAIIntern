import pandas as pd
import requests
import json

REST_API_KEY = '17c0b9f74fc85063050894f4653052d1'

def kogpt_api(prompt, max_tokens = 1, temperature = 1.0, top_p = 1.0, n = 1):
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/kogpt/generation',
        json = {
            'prompt': prompt,
            'max_tokens': max_tokens,
            'temperature': temperature,
            'top_p': top_p,
            'n': n
        },
        headers = {
            'Authorization': 'KakaoAK ' + REST_API_KEY,
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response

prompt='''주어진 문장을 존댓말 문장으로 바꿔주세요.

문장:하지마!
존댓말:하지 말아주세요.

문장:나랑 같이 놀러가자
존댓말:저랑 같이 놀러가지 않으실래요?

문장:배고파 밥줘
존댓말:배가고픈데 밥을 먹어도 될까요?

문장:그거 재밌어?
존댓말:그것은 재미 있나요?

문장:뭐하는거야 지금
존댓말:지금 무엇을 하시는 건가요?

문장:런던 금속 거래소에서 망간 가격 찾는 방법 알려죠
존댓말:'''
response = kogpt_api(prompt, max_tokens=100, temperature=0.7)

print(response['generations'][0]['text'])