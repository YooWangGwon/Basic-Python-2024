# file : test42_pypaint.py
# date : 20240206
# desc : 그림판 만들기

import sys
from PyQt5 import uic # Qt Designer호출시 필요
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *

class Winapp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self):
        # uic.loadUi('./day07/pyPaint.ui', self) # 화면초기화
        uic.loadUi('C:/Sources/basic-python-2024/day07/pyPaint.ui', self) # 실행파일 생성시는 경로에 상대경로가 없어야함
        # self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowIcon(QIcon('C:/Sources/basic-python-2024/day07/iot.png')) # 실행파일 생성시는 경로에 상대경로 제거
        self.setWindowTitle('Py그림판')
        # 캔버스 초기화
        self.brushColor = Qt.black
        self.canvas = QPixmap(self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QColor('white'))
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.setStyleSheet('background:black;')
        self.btn_red.setStyleSheet('background:red;')
        self.btn_blue.setStyleSheet('background:blue;')    

        self.setCenter
        self.show()

    def initSignal(self): # 동작초기화
        self.btn_black.clicked.connect(self.buttonClicked)
        self.btn_red.clicked.connect(self.buttonClicked)
        self.btn_blue.clicked.connect(self.buttonClicked)
        self.btn_clear.clicked.connect(self.buttonClicked)
        # 이미지 로드 및 저장버튼 추가
        self.btn_load.clicked.connect(self.btnLoadClicked)
        self.btn_save.clicked.connect(self.btnSaveClicked)

    def btnLoadClicked(self): # 이미지 로드
        image = QFileDialog.getOpenFileName(None, '이미지로드', '', 'Image file(*.jpg;*.png)')
        imagePath = image[0]
        # print(imagePath)
        pixmap = QPixmap(imagePath).scaledToHeight(381) # 파일 경로에 있는 이미지를 읽어서 pixmap 객체에 담는다
        self.lb_canvas.setPixmap(pixmap)
        self.lb_canvas.adjustSize() # 이미지를 라벨 크기에 맞춤

    def btnSaveClicked(self): # 이미지 저장
        filePath, _ = QFileDialog.getSaveFileName(self, '이미지저장', '', 'Image file(*.jpg;*.png)')
        if filePath == '':return
        pixmap = self.lb_canvas.pixmap()
        pixmap.save(filePath)

    def buttonClicked(self): # black, red, blue를 다 통일한 함수
        btn_val = self.sender().objectName()
        print(btn_val)
        if btn_val == 'btn_black': # 검은색 버튼 클릭
            self.brushColor = Qt.black
        elif btn_val == 'btn_red': # 빨간 버튼 클릭
            self.brushColor = Qt.red
        elif btn_val == 'btn_blue': # 파란 버튼 클릭
            self.brushColor = Qt.blue
        elif btn_val == 'btn_clear': # 클리어 버튼 클릭
            self.canvas.fill(QColor('white')) # 캔버스를 흰색으로 채운다
            self.lb_canvas.setPixmap(self.canvas)

    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap()) # 브러쉬
        brush.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap))
        brush.drawPoint(e.x(), e.y())
        brush.end
        self.update() # 화면 업데이트
    
    def setCenter(self): ## Winapp을 화면 정중앙에 위치
        gm = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center() 
        gm.moveCenter(cp) 
        self.move(gm.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = Winapp()
    sys.exit(app.exec_()) # 종료시 리소스 반환등 효율증가