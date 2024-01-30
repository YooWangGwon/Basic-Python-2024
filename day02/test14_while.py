# file : test14_while.py
# date : 20240130
# desc : while 문

## while 참인 조건 : 
### 공통점 - if 조건: elif 조건: else: , for in range():, while 조건:

count = 0

# while count < 10: # count 변수값이 10보다 작거나 같은 동안 반복
# 무한루프 : Window OS, 모바일 OS, 자동차 네비게이션, 라즈베리파이, 아두이노, 게임, Winform개발, 웹개발 등에서 활용

while True: # 조건이 참인동안 = True : 항상 참
    count = count + 1
    print('나무찍기를', count,'번 했다.')
    if count == 10:
        print('나무가 쓰러졌다!')
        break # 이 반복문을 빠져나가라
        

number = 0
while True:
    number = number + 1
    if str(number).count('3') >= 1 or\
        str(number).count('6') >= 1 or\
        str(number).count('9') >= 1: # 숫자를 문자열로 바꾼 값안에 '3', '6', '9'가 있으면
        print('짝!') # 짝! 대신 continue로 변경
        # continue는 반복에서 제외할 뿐 반복을 종료하는것은 아님
    else:
        print(number)
    if number == 30: 
        break # 반복문을 완전히 빠져나감