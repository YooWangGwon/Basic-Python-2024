# 파이썬 기초 2024
부경대학교 2024 IoT 개발자 과정 기초 프로그래밍 언어 - 파이썬

## 1일차
- 개발환경 구축
    - 코딩폰트 - 나눔고딕코딩
    - Notepad++ 설치
    - Python 설치
    - Visual Studio Code 설치
    - Git 설치
        - TortoiseGit 설치
        - Github 가입
        - Github Desktop 설치

- 파이썬 기초
    - 콘솔출력
    - 주석
    - 변수
    - 자료형
    - 연산자

    ```python
    # 이 부분은 주석입니다.
    var01 = 10 # 정수, 실수, 불, 문자열 모두 가능
    print(var01)
    print(type(var01))

    print(5 + 4 / 2) # 7.0
    print(5 == 4) # False
    ```

## 2일차
- 파이썬 기초
    - 흐름제어
        - if : Ture/False로 조건 분기 (다른 언어 switch)
        - for : 반복문 기본 (다른 언어 foreach)
        - while : 반복문 변형 (다른 언어 do~while)
    - 복합자료형 + 연산자
        - 리스트, 튜플, 딕셔너리
    - 출력 포맷
    - 구구단 + 디버깅

    ```python
    # debugging
    # F9(중단점 토글), F5(디버그 시작), F10(한줄씩 실행), F11(함수안으로 진입)
    # Shift + F5(디버깅 종료)
    print('구구단 시작!')
    for x in range(2, 9+1): # 2부터 9까지 반복
        print(f'{x}단------>')
        for y in range(1, 9+1): # 1부터 9까지 반복
            print(f'{x} x {y} = {x*y:2d}', end=' ') # end=' ' : 엔터 대신 공백으로 변경
        print() # 안쪽 for 문이 끝나면 마지막 엔터를 하나 추가
    ```

## 3일차
- 파이썬 기초
    - 입력 방법
    - 별찍기(피라미드 만들기)
    - 함수(람다함수는 나중에)
    - 객체지향(OOP:Object Oriented Programming)
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아둔 곳 : 클래스(class)
        - 클래스에서 하나씩 생성하는 것 : 객체(object)
        - 클래스(class)는 설계도, 객체(object)는 설계도로 구현한 대상
        - 캡슐화(test22 : __plate_num 참조)
    - 패키지, 모듈

## 4일차
- 파이썬 기초
    - 패키지, 모듈 계속
        - pip 사용

        ```shell
        > pip --version # pip 버전 확인
        > pip list # 현재 설치된 라이브러리 목록 확인
        > pip install 패키지명 # 패키지를 내 컴퓨터에 설치, Successfully installed 문구 확인할 것
        > pip unistall 패키지명 # 패키지를 내 컴퓨터에서 삭제
        ```
    - 예외처리 : 비정상적인 프로그램 종료 방지

    ```python
    file : test27_eh.py
    def divide(x, y): 
        try:
            return x / y # ZeroDivision 발생 주의
        except ZeroDivisionError as e:
            print('[오류] 제수는 0이 될 수 없습니다.')
            return 0
    ```
    
    - 텍스트 파일 입출력
- 파이썬 활용
    - 주피터 노트북



    - 객체지향(추후 학습 예정)
        - 오버로딩, 오버라이딩(재정의)
        - 상속, 다중상속
        - 추상클래스
    - 가상 환경