# file : test20_function.py
# date : 20240131
# desc : 함수 만들기(계산기 기능)

def add(x,y) -> int:
    result = x + y
    return result

def minus(x,y) -> int:
    result = x - y
    return result

def multi(x,y) -> int:
    result = x * y
    return result

def divide(x,y) -> float:
    result = x / y
    return result

a, b = map(int,input('두 정수입력 >').split(' '))
결과 = add(a,b)
print(f'{a} + {b} = {결과}')
print(f'{a} - {b} = {minus(a,b)}')
print(f'{a} x {b} = {multi(a,b)}')
print(f'{a} ÷ {b} = {divide(a,b)}')

def say_hello() -> None:
    print('Hello')
    # return None -> None을 return하기 때문에 의미가 없기 때문에 생략되어 직접 입력할 필요X 


def say_hello2(name):
    print(f'Hello, {name}')

say_hello()

say_hello2('WG Yoo')