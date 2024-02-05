# file : test36_pyqt.py
# date : 20240205
# desc : PyQt5 기본화면 만들기

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QFont 
from PyQt5.QtWidgets import QApplication, QWidget # 색이 흐린 것은 가져오고 사용하지 않음을 의미

# print(sys.argv) # 현재 파이썬 파일의 경로 표시

class qtwin_exam(QWidget): # QWidhet을 상속받을거야 -> QWidget이 가진 모든 것을 사용할 수 있다
    # 생성자
    def __init__(self) -> None: # self : 나
        super().__init__() # super : 부모, QWidget
        self.initUI() # 화면초기화 함수를 호출

    def initUI(self):
        self.setGeometry((1920-400)//2, (1080-300)//2, 400, 300) # 윈도우 앱 화면을 만들겠다. # x, y, width, height
        self.setWindowTitle('Qt5 Hello world!')
        self.text = ''
        self.show()

    def drawText(self, event, paint):
        paint.setPen(QColor(10, 10, 10)) # dark gray / r0,g0,b0 -> black/ r255,g255,b255 -> white
        paint.setFont(QFont('Nanumgst[othinc', 15))
        paint.drawText(300//2, 300//2 ,'HELLO WORLD!')
        paint.drawText(event.rect(), Qt.AlignLeft, self.text) # AlignLeft, AlignCenter, AlignRight
    
    def paintEvent(self, event) -> None: # 재정의(Overload)
        paint = QPainter()
        paint.begin(self) # 열기
        self.drawText(event, paint)
        paint.end() # 닫는다

loop = QApplication(sys.argv) # 내 소스의 위치로 앱을 생성 
isinstance = qtwin_exam() # QWigdet을 상속한 qtwin_exam 객체를 생성
loop.exec_()