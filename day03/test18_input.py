# file : test18_input.py
# date : 20240131
# desc : 다중입력

# 원래는 (input_a, input_b) 튜플형으로 데이터 받는게 정석 -> 이번에는 생략
# 1. 두 수를 받을 때 가장 원시적인 방법
# input_a, input_b= input('값을 두개 입력(공백으로 구분) > ').split(' ')
# input_a = int(input_a)
# input_b = int(input_b)

# 2. map() 함수 사용 - 소스코드가 줄어들어 더 많이 사용됨
input_a, input_b = map(int, input('값을 두개 입력(공백으로 구분) > ').split(' ')) # 한번에 문자열형에서 정수형으로 변환

print(f'입력값 {input_a},{input_b}')
print(f'더하기 결과 {input_a + input_b}')