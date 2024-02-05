# file : test37_pyqt.py
# date : 20240205
# desc : PyQt5 이벤트(Signal)

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        btn01 = QPushButton('클릭',self)
        btn01.setGeometry(50, 100, 100, 40) # 위치는 x=50, y=100에 크기는 width=100, height = 40
        btn01.clicked.connect(self.btn01_clicked) # 버튼을 클릭하면(시그널) btn01_clicked 함수를 연결해 실행시키겠다.
    

        self.setGeometry(300,200,400,200)
        self.setWindowTitle('버튼 시그널')
        # self.show()

    def btn01_clicked(self): # 버튼(btn01) 클릭시 실행되는 함수
        QMessageBox.about(self, '버튼클릭','버튼을 클릭했습니다')

    def closeEvent(self,QCloseEvent) -> None: # X버튼 종료확인
        re = QMessageBox.question(self,'종료확인','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == '__main__': # Main Entry인지 확인하는 조건 추가
    loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성
    isinstance = qtwin_exam() # Qtwidget을 상속한 qtwin_exam 객체를 생성
    isinstance.show()
    loop.exec_()