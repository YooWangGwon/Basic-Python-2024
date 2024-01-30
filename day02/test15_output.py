# file : test15_output.py
# date : 20240130
# desc : 콘솔 출력 포맷양식 String Format

string_1 = '{}'.format(10) # {}위치에 함수 뒤에 들어있는 값을 치환, !원하는 양식!으로 표현
print(string_1)
print(type(string_1))

name= '유왕권' #input('이름 입력 > ')
string_2 = '안녕하세요, {}입니다!'.format(name)
print(string_2)

string_3 = '{},{},{}'.format(4000,'만','빌려주세요')
print(string_3)

# 정수를 문자열포맷 d(★★★★★)
# = : 기호와 숫자를 분리, 05 : 다섯자리 만들 때 빈자리 0으로 채우기, d : 정수, 02d : 두자리 수 만들 때 빈자리 0으로 채우기
string_4 = '_____{:=+5d}_____'.format(-100) # 텍스트를 출력하는 공간을 마련해둔 것
print(string_4)

# 실수 문자열포맷 f ( 기본 소수점 6자리 )(★★★★★)
# 7.2f 전체 자리수를 7자리로, 소수점 뒤는 2자리로 fix
val = 78.333333333
string_5 = '_____{:7.2f}_____'.format(val)
print(string_5)

# python 3.6 이후 도입. format 함수 아예 사용안함(★★★★★)
val = 78.333333333
string_6 = f'_____{val:7.2f}_____' # string_5보다 편리함!!
print(string_6)

string_7 = 'Hello, World!'
print(string_7.upper()) # upper case : 문자를 모두 대문자로 변환
print(string_7.lower()) # lower case : 문자를 모두 소문자로 변환
print(string_7.lower().capitalize()) # capitalize case : 첫번째 글자만 대문자로 변환
print(string_7.split(',')) # 특정한 단어(쉼표)를 기준으로 자르는 함수

string_8 = 'Hello, I am WG YOO. I am a student. Good Luck for your day.'
words = string_8.split(' ') # 특정한 단어(공백)를 기준으로 자르는 함수
print(words)
print(f'문장의 단어 갯수는 {len(words)}개 입니다.')

string_9 = 'A10'
print(string_9.isalnum()) # True : 숫자와 알파벳만 가능 / A10+ 일 경우에는 False
print(string_9.isnumeric()) # False :  숫자만 가능

string_10 = '10.5'  # 소수점은 함수를 만들어서 처리해야함
print(string_10.isdecimal()) # False

print('안녕'in'안녕하세요') # True : '안녕하세요' 안에 '안녕'이라는 단어가 있는지 확인
print('안냥'in'안녕하세요') # False : 문장 안에 단어가 없음