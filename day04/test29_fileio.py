# file : test29_fileio.py
# date : 20240201
# desc : 텍스트 파일 읽기

f = open('sample.txt', mode = 'r', encoding='utf-8')
# 아래의 방법은 기초적이나 용량문제로 큰 파일은 읽는 것은 불가하다
# text = f.read() # 텍스트 파일 내 모든 텍스트를 전부 한번에 읽어온다.(지나치게 많은 텍스트는 모두 읽지 못한다.)
# print(text)

# 아래는 가장 일반적
while True:
    line = f.readline() # 한줄씩 읽기
    if not line : break # 조건문, 반복문 내의 코드가 한줄만 있으면 if문 옆에 바로 적을 수 있다.
    print(line.replace('\n','')) # replace로 \n을 빈값으로 교체하여 엔터가 두번 생기는 것을 방지

f.close()