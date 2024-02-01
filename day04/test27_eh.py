# file : test27_eh.py
# date : 20240201
# desc : 예외발생 처리

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def multi(x, y):
    return x * y

def divide(x, y): 
    try:
        return x / y # ZeroDivision 발생 주의
    except ZeroDivisionError as e:
        print('[오류] 제수는 0이 될 수 없습니다.')
        return 0
    
# 한번 이상 반복되는 소스코드는 함수로 만들어놓아야한다!!

def getOperands(): # 계산할 수를 입력받는 함수
    # 34. 을 넣었을 때 예외발생 ValueError
    try : 
        a, b = map(int,input('두 수 입력(구분자 공백) > ').split(' '))
        return a, b
    except ValueError as e:
        # print(e) # 정확한 예외 메시지 출력
        print('입력 오류 : 정수만 입력하시오')
        return 1, 1

while True:
    mnu = input('메뉴입력(p[덧셈],m[뺄셈],t[곱셈],d[나눗셈],x[종료]) > ')

    if mnu == 'p':
        a, b = getOperands()
        print(f'덧셈 {a} + {b} = {add(a, b)}')
    elif mnu == 'm':
        a, b = getOperands()
        print(f'뺄셈 {a} - {b} = {minus(a, b)}')
    elif mnu == 't':
        a, b = getOperands()
        print(f'곱셈 {a} x {b} = {multi(a, b)}')
    elif mnu == 'd':
        a, b = getOperands()
        print(f'나눗셈 {a} ÷ {b} = {divide(a, b)}')
    elif mnu == 'x':
        print('계산기 종료')
        break
    else:
        continue # 다시 메뉴 선택으로 올라감