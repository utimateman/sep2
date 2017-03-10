import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("draw")

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon([QPoint(70, 100), QPoint(100, 110),
                       QPoint(130, 100), QPoint(100, 150),
                       ])

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon([
                QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),
        ])
class Simple_drawing(Simple_drawing_window1):
    def __init__(self):
        Simple_drawing_window1.__init__(self)
        

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 221, 0))
        p.drawPolygon([QPoint(250, 100), QPoint(250, 300),
                       QPoint(300, 190)
                       ])

        p.setPen(QColor(255, 255, 0))
        p.setBrush(QColor(255, 255, 0))
        p.drawPolygon([
                QPoint(50, 100), QPoint(250, 100), QPoint(50, 300),QPoint(250, 300)
        ])



def main():
        app = QApplication(sys.argv)

        w = Simple_drawing()
        w.show()
        

        return app.exec_()

if __name__ == "__main__":
        sys.exit(main())
