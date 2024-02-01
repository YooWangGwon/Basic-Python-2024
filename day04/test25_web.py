# file : test25_web.py
# date : 20240201
# desc : urllib 모듈 사용법

from urllib.request import * # request 모듈 안의 모든 내용을 사용할 때, from urllib.request와 크게 다르지 않다
from urllib.request import Request, urlopen # Request 클래스와 urlopen만 쓰겠다.

req = Request('https://www.naver.com/') # 네이버 웹주소(url)
res = urlopen(req) # url 주소로 뭽사이트를 열어달라고 요청

print(f'응답코드 : {res.status}') # url로 요청된 웹사이트 응답 확인 
print(res.read())

import requests # urllib.request보다 성능이 조금 더 우월

res2 = requests.get('https://www.naver.com/')

print(res2.status_code)
print(res2.text)