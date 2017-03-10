from PySide.QtGui import *
from PySide.QtCore import QTimer
import PySide.QtCore as QtCore

class W(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(400,400)
        self.myIsMousePressing = False
        self.p = QPainter(self)
        self.autoFillBackground()
        self.x = 0
        self.y = 0
        self.r = dict()#{(x,Y,49, 49):rect}
        self.penColor = 1
        self.button = QPushButton('Clear', self)
        self.button.clicked.connect(self.clear)
    def clear(self):
        self.r = dict()
        self.update()
    def mousePressEvent(self, event):
        self.myIsMousePressing = True
    def mouseReleaseEvent(self, event):
        self.myIsMousePressing = False
    def myTimeOut(self):
        if self.myIsMousePressing:
            pos = self.mapFromGlobal(QCursor.pos())
            self.x = pos.x()/50
            self.y = pos.y()/50
            self.r[(self.x*50, self.y*50, 10, 10)] = self.penColor
    def paintEvent(self, event):
        self.p.begin(self)
        for k in self.r.keys():
            if self.r[k] == 1:
                self.p.setPen(QtCore.Qt.black)
                self.p.setBrush(QtCore.Qt.black)
            else:
                self.p.setPen(QtCore.Qt.white)
                self.p.setBrush(QtCore.Qt.white)
            self.p.drawRect(*k)
        self.p.end()
        self.update()

class MyWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(400, 400)
        self.w = W()
        self.setCentralWidget(self.w)
        self.t = QTimer(self.w)
        self.t.timeout.connect(self.w.myTimeOut)
        self.t.start(1)

    def initMenu(self):
        self.button = QPushButton('Clear', self)
        self.button.clicked.connect(self.clear)

app = QApplication([])
mainWin = MyWidget()
mainWin.show()
app.exec_()
