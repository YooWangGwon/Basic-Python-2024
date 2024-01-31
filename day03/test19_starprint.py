# file : test19_starprint.py
# date : 20240131
# desc : 별찍기 또는 피라미드 만들기

for i in range(1,6):
    print(i * '*')

for i in range(1,10):
    print(' '*(9-i),(i*2-1)*'*')

for j in range(9,-1,-1):
    print(' '*(9-j),(j*2-1)*'*')

for i in range(1,5+1):
    # 첫번째 i가 1일 때는 range가 (1,2) -> 1번 반복
    # i가 2이면, range(1,3) 2번 반복
    for j in range(1, 5-i+1):  
        print(' ', end='') # 엔터대신 empty로 변환
    for j in range(1, i+1):
        print('*', end='')
    print() # 안쪽 for문이 끝나면 엔터

for i in range(1,5+1):
    for j in range(1, 5-i+1):  
        print(' ', end='')
    for j in range(1, i*2):
        print('*', end='')
    print()