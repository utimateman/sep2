from turtle import *
class Disk():

    def __init__(self,name="",xpos=0,ypos=0,height=20,width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        lt(90)
        pu()
        goto(self.dxpos,self.dypos)
        pd()
        rt(90)
        for x in range(2):
            fd(self.dwidth/2)
            lt(90)
            fd(self.dheight)
            lt(90)
            fd(self.dwidth/2)

    def newpos(self,xpos,ypos):
        self.dxpos = xpos
        self.dypos = ypos
        
    def cleardisk(self):
        pencolor("WHITE")
        self.showdisk()
        pencolor("BLACK")
        
