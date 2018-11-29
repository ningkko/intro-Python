# CatFace
# Simin Saba Royesh & Yining Hua
# Lab#3


from graphics import *

def main():
        win = GraphWin('CatFace', 500,500)
        win.setBackground("black")
        win.setCoords(-100,-100,100,100)

        catE1 = Polygon(Point(-65,100),Point(-65,0),Point(0,80))
        catE1.setFill("pink")
        catE2 = Polygon(Point(65,100),Point(65,0),Point(0,80))
        catE2.setFill("pink")

        catFace = Oval(Point(-80,-50), Point(80,90))
        catFace.setFill("white")

        catEye1 = Circle(Point(-35,35), 10)
        catEye1.setFill("yellow")
        catEye2 = Circle(Point(35,35),10)
        catEye2.setFill("yellow")

        catPupil1 = Circle(Point(-35,35),5)
        catPupil1.setFill("black")
        catPupil2 = Circle(Point(35,35),5)
        catPupil2.setFill("black")

        catNose = Polygon(Point(13,8),Point(0,-5),Point(-13,8))
        catNose.setFill("pink")

        catM = Polygon(Point(0,-5),Point(-4,-20),Point(4,-20))
        catM.setFill("red")

        
        catE1.draw(win)
        catE2.draw(win)
        catFace.draw(win)
        catEye1.draw(win)
        catEye2.draw(win)
        catPupil1.draw(win)
        catPupil2.draw(win)
        catNose.draw(win)
        catM.draw(win)

        
        win.getMouse()
        win.close()
	
	
        
main()
