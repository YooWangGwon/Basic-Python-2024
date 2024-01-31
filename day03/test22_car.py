# file : test22_car.py
# date : 20240131
# desc : Car 클래스 만들기

class Car:
    wheel_num = 4
    color = 'white'
    __plate_num = '' # __'멤버변수' : 외부에서 차량번호를 변경할 수 없도록 막는 조치
    company = ''
    gear_type = ''

    # 전진, 후진, 좌회전, 우회전 -> 함수
    def moveForward(self):
        print(f'차량번호 {self.__plate_num}이 전진합니다.')
    
    def moveBackward(self):
        print(f'차량번호 {self.__plate_num}이 후진합니다.')

    def moveLeft(self):
        print(f'차량번호 {self.__plate_num}이 좌회전합니다.')
        
    def moveRight(self):
        print(f'차량번호 {self.__plate_num}이 우회전합니다.')

    # 생성자를 변경하여 변경된 생성자로 호출해야한다. -> number, comp, col, gear 값들을 입력해줘야한다.
    def __init__(self, __plate_num, company, color, gear_type) -> None: 
        self.__plate_num = __plate_num # 매개변수에 있는 plate_num와 self.옆에 있는 plate_num(멤버변수)은 다르다. 작업상 편의를 위해 이름을 맞추는 것이 좋다.
        self.company = company
        self.color = color
        self.gear_type = gear_type

    def __str__(self) -> str:
        return f'제 차는 {self.__plate_num}입니다. 차량 색상은 {self.color}입니다.'
    
    def getPlateNumber(self): # 외부에서 차량번호를 변경할 수 없도록 막는 조치
        return self.__plate_num

    def setPlateNumber(self, new_PlateNumber):
        self.__plate_num = new_PlateNumber

sarah = Car('23가4567','현대자동차','화이트','자동') # 객체 생성
# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있다.
print(sarah)
# print(f'차량번호는 {sarah.plate_num}')
print(f'차량 색상은 {sarah.color}')
sarah.moveForward()

sarah.__plate_num = '44하7789' # 악의적인 의도를 가지고 변경
print(sarah)

sarah.setPlateNumber('54로9555') # 클래스에서 인정받은 동작(함수)으로 값을 변경
print(sarah)

csuv = Car('경남88 1922','기아자동차','회색','자동')
print(f'차량번호는{csuv.__plate_num}')