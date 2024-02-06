# file : test41_exam.py
# date : 20240206
# desc : PyQt5 이미지 뷰터

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class Winapp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        # 이미지 추가. scaleToWidth(800) : 큰 해상도를 넓이 w:800으로 고정
        pixmap = QPixmap('./images/kitty.jpg').scaledToWidth(800)
        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)

        lblSize = QLabel(self)
        lblSize.setFont(QFont('맑은 고딕', 20, QFont.Bold)) # 폰트와 폰트사이즈
        lblSize.setStyleSheet('Color : blue') # 폰트 색상 변경
        lblSize.setText(f'{pixmap.width()}x{pixmap.height()}') # kitty.jpg의 width x height
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) # 가로중앙정렬 | 세로중앙정렬

        vbox = QVBoxLayout(self) # QtDesigner에서 VerticalLayout 위젯 생성
        vbox.addWidget(lblImage) # VL에 위젯 추가 
        vbox.addWidget(lblSize) 
        self.setLayout(vbox) # Form에 VL 추가와 동일

        self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowTitle('이미지뷰어')
        rect = QRect(300, 300, 300, 300) # x, y, w, h
        self.setGeometry(rect) # 같은 이름의 함수를 여러개 선언해놓고 입맛에 맞게 골라쓰는 것 BR(오버로딩)
        # self.setGeometry(300,300,300,300)
        self.setCenter()
        self.show() # showFullScreen() : 모니터를 꽉 채워서 출력 

    def setCenter(self): ## Winapp을 화면 정중앙에 위치
        gm = self.frameGeometry() # 현재 Winapp 자신의 위치값
        cp = QDesktopWidget().availableGeometry().center() # 현재 모니터의 정중앙 값
        win_rsl = QDesktopWidget().availableGeometry() #모니터 해상도 구하는 법
        print(f'{win_rsl.width()} x {win_rsl.height()}')
        gm.moveCenter(cp) 
        self.move(gm.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    width, height = screen_rect.width(), screen_rect.height()
    print(width, 'x', height) # 활용도가 높음
    ins = Winapp()
    sys.exit(app.exec_()) # 종료시 리소스 반환등 효율증가