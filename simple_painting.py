import sys
import random
from PySide.QtCore import *
from PySide.QtGui import *

class Rabbit:
        def __init__(self, x, y):
                self.x = x
                self.y = y
                ##self.x = 0
                
        
        def paintEvent(self, e):
                p = QPainter()
                p.begin(self)
                p.setPen(QColor(0,0,0))
                p.setBrush(QColor(0,127,127))
                p.drawPolygon([QPoint(self.x,self.y), QPoint(self.x,self.y+10), QPoint(self.x + 10, self.y + 10), QPoint(self.x+10,self.y)])
                p.end()

        
        '''
        def draw(self, x, y):
                p = QPainter()
                p.begin(self)
                p.setPen(QColor(0,0,0))
                p.setBrush(QColor(0,127,127))
                p.drawPolygon([QPoint(self.x,self.y), QPoint(self.x,self.y+10), QPoint(self.x + 10, self.y + 10), QPoint(self.x+10,self.y)])
                p.end()
        '''

class Animation_area(QWidget):
        def __init__(self):
                QWidget.__init__(self, None)
                self.setMinimumSize(500, 500)

                self.arena_w = 500
                self.arena_h = 500
                
                ##self.rabbit = Rabbit()
                #self.timer = QTimer(self)
                #self.connect(self.timer, SIGNAL("timeout()"), self.update_value)
                #self.timer.start(1000)

        def mousePressEvent(self, e):
                self.rabbit = Rabbit(e.pos().x(), e.pos().y())
                self.x = e.pos().x()
                self.y = e.pos().y()
                
        def paintEvent(self, e):
                p = QPainter()
                p.begin(self)
                ##self.rabbit.draw(self.x, self.y)
                p.end()

        def update_value(self):
                   self.rabbit.random_pos(self.arena_w, self.arena_h)
                   self.update()

      

class Simple_animation_window(QWidget):
        def __init__(self):
           QWidget.__init__(self, None)

           self.anim_area = Animation_area()

           layout = QVBoxLayout()
           layout.addWidget(self.anim_area)

           self.setLayout(layout)
           self.setMinimumSize(530, 600)

def main():
           app = QApplication(sys.argv)

           w = Simple_animation_window()
           w.show()

           return app.exec_()

if __name__ == "__main__":
        sys.exit(main())

                        
