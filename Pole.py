from turtle import *

class Pole():

    def __init__(self,name="",xpos=0,ypos=0,thick=10,length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        lt(90)
        pu()
        goto(self.pxpos,self.pypos)
        pd()
        rt(90)
        for x in range(2):
            fd(self.pthick/2)
            lt(90)
            fd(self.plength)
            lt(90)
            fd(self.pthick/2)
    def pushdisk(self,disk):
        disk.newpos(self.pxpos,self.toppos)
        disk.showdisk()
        self.stack.append(disk)
        self.toppos += disk.dheight
        self.toppos += 1

    def popdisk(self):
        d = self.stack.pop()
        d.cleardisk()
        self.toppos -= 1
        self.toppos -= d.dheight
        return d


    
