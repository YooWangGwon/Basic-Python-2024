# file : test28_fileio.py
# desc : 텍스트 파일 입력

# mode : a(ppend:내용추가) r(ead:파일읽기) w(rite:파일쓰기) -> 파일의 용도
# encoding : cp949(euc-kr:한글), utf-8(만국공통어) -> 읽어올 때 사용할 언어
f = open('sample.txt', mode='w', encoding='utf-8') # 파일의 이름, 용도, 읽어올 언어를 지정하고 오픈

# write()에서 엔터를 추가하려면 마지막에 \n 을 해야한다.
f.write('안녕하세요. 우리는 IoT개발자 과정입니다.\n') # mode = a, w : 작성하는건 a또는 w만 된다 
f.write('반갑습니다.\n')

f.close() # 파일은 무조건 마지막에 닫는다.
print('파일이 생성되었습니다.')