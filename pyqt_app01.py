import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("첫코딩화면")
        

# Application 만들기
app = QApplication(sys.argv)

# 세부기능 만들기
window = MyWindow()

window.show()

# 실행코드
app.exec_()