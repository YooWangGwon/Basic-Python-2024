# file : test23_module.py
# date : 20240131
# desc : 모듈 사용

# 한 폴더에 관련된 모듈들만을 모아둔 집합을 패키지라고 한다.

import math # C언어 표준에 정의되어 있는 수학적인 함수들을 접근할 수 있게 함

PI = 3.141592
radius = 5
print(f'원의 크기는{radius*radius*PI}이다')

print(math.pi)
print(f'정확한 원의 크기는 {radius*radius*math.pi}')

print(f'cos(0) = {math.cos(0)}')
print(2 ** 10)
print(math.pow(2,10))
print(math.ceil(3.1)) # 올림
print(math.floor(3.5)) # 내림
print(round(3.5)) # 반올림 : 사용빈도가 높아 math에 있는게 아닌 기본함수에 편성되어 있다.

import math as m # 별명짓기. 이름이 긴 모듈을 사용할 때 활용
print(m.sin(1))

from math import pi, pow # 조심해서 사용, math.을 붙이지 않아도 됨, 다른모듈에 있는 동일한 이름의 다른 내용과 충돌가능성 있음

print(pi) 
print(pow(2,10))