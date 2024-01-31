# file : test21_oop.py
# date : 20240131
# desc : 객체지향 클래스 만들기

# 클래스(사람이라는 객체를 만들기 위한 청사진) 만들기
class Person: # 사람 클래스 선언
    name = '' # name, age, gender : 클래스 안에 속하는 멤버 변수 -> 객체를 설명해주는 변수
    age = 0
    gender = ''

    # 멤버함수(클래스의 멤버 함수)
    def walk(self): # self : 객체 자신 -> 멤버함수를 지정할 때는 매개변수로 self가 필수이다.
        print(f'{self.name}이(가) 걷습니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

    # 생성자 : 객체를 생성하는데 사용되는 함수
    # 파이썬에서 기본적으로 제공하는 기본생성자가 있음
    # 생성자 함수 : 클래스에 속하는 스페셜 함수, 클래스의 객체를 생성할 때 동작.
    # init == initialization(초기화) -> 객체가 생성될 때 초기화 과정을 한번 거치고 생성되기 때문
    def __init__(self) -> None: # 스페셜 함수 : __'함수'__
        self.name = '홍길동'   # 생성자는 return값이 없다.
        self.age = 29
        self.gender = '남자'

    # 클래스를 호출할 때 나온 결과를 원하는 형태로 변환해서 보여줄 때 아래 함수를 사용
    def __str__(self) -> str:
        strs = f'커스텀 출력, 이름: {self.name} 객체 생성!'
        return strs

# 사람 객체 생성, Instance(사례, 예제) = 만들어진 객체
wg = Person() # 클래스를 사용할 때는 괄호에 넣을 내용이 없더라도 괄호를 사용해야한다. 함수호출처럼 작성하면 됨
es = Person() # 같은 Person 클래스 일지라도 mg와 es는 서로 다른 객체이다

print(type(wg))
print(id(wg)) # 객체의 고유한 id
print(id(es))

wg.name = '유왕권' # . 은 wg라는 객체에 속하는 변수라는 의미
wg.age = 25 
wg.gender = '남자' 

es.name = '애슐리'
es.age = 30
es.gender = '여자'

print(f'wg => {wg.name} / {wg.age} / {wg.gender}')
print(f'es => {es.name} / {es.age} / {es.gender}')

wg.walk() # 클래스의 멤버 함수이기 떄문에 별도의 매개변수를 입력하지 않아도 된다.
print('1분동안 걷는다')
wg.stop()

es.walk()
print('걷기 싫어함')
es.stop()

print('생성자 함수 추가--------------------------->')
gd = Person() # 생성자 함수를 설정한 후에는 객체의 name, age, gender에 별도의 값을 지정하지 않는다면 '홍길동 / 29 / 남자'로 고정된다.
print(f'gd => {gd.name} / {gd.age} / {gd.gender}')
print(gd)