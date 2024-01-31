# file : test17_input.py
# date : 20240131
# desc : 콘솔 입력

# 출력 - 컴퓨터 화면, 프린터, 스피커, 빔프로젝터, VR, ...
# 입력 - 컴퓨터 상에서 콘솔 입력(키보드), 마우스 입력, 목소리, 조이스틱, 터치스크린, ...
# input('입력을 원하는 내용 추가') - 반드시!!

temp_val = input('곱할 수 입력 > ')
if temp_val.isnumeric() == True: # 입력된 temp_val이 정수인가??
    temp_val = int(input('곱할 수 입력 > ')) # 문자열형에서 정수형으로 변환(형 변환)
    print(f'입력값 = {temp_val}')

# 곱하기 
    result = temp_val * 5
    print(f'결과 = {result}') # 형 변환을 하지 않으면 result가 10001000100010001000으로 출력됨
else: # 입력된 temp_val이 정수가 아닐 경우
    print('잘못된 입력, 정수만 입력하세요.')