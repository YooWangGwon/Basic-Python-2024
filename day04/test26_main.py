# file : test26_main.py
# date : 20240201
# desc : __main__ 에 대한 내용

# entry point : 프로그램을 구성하는 파일들 중에서 메인이 되어 다른 파일들을 이끌고 가는 선두적인 파일

class Temp:
    pass

if __name__ == '__main__': # 현재 스크립트 파일이 프로그램의 시작점이 맞는지 판단하는 작업
    print('제가 시작점입니다.')
    tt = Temp()
    print(type(tt))

