#Yining Hua & Mariya Germash
#Bar.py = lab#4
#A program draws bars


from graphics import *
from random import*

def main():
        #revisible local variables
	x,y = -65,-80
	height,width= 150,20
	win = GraphWin('Bar', 500,500)
	win.setBackground("lightslateblue")
	win.setCoords(-100,-100,100,100)

        #printing text
	t = "My Feeling v.s. Size of the Class"
	title = Text(Point(0,-90), t)
	title.setSize(14)
	title.setTextColor("pink")
	title.draw(win)

	#draw bars and heads for (height/width) times
	for i in range(height,0,-width):
		Bar(x,y,width,height,win)
		height=height-width
		x = x + width



		
def Bar(x,y,width,height,win):
	'''draws a bar,(x,y,width,height,win)
	'''
	bar = Rectangle(Point(x-width/2,y),Point(x+width/2,y+height))
	bar.setFill("pink")
	bar.draw(win)
	Head(x,y+height,width,win)

def Head(x,y,radius,win):
	'''draws a head(x,y,radius,win)
	'''
	head = Circle(Point(x,y),(radius/2))
	head.setFill("yellow")
	head.draw(win)
	
	eye1 = Circle(Point(x-radius/4,y+radius/6),radius/15)
	eye1.setFill("gray")
	eye1.draw(win)
	
	eye2 = Circle(Point(x+radius/4,y+radius/6),radius/15)
	eye2.setFill("gray")
	eye2.draw(win)
	
	mouth = Polygon(Point(x,y),
			Point(x-radius/4,y-radius/5),
			Point(x+radius/4,y-radius/5))
	mouth.setFill("red2")
	mouth.draw(win)

main()


