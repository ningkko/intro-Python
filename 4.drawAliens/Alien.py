#Yining Hua
#assignment 4
#Draws a picture of aliens by calling the function AlienHead()
#which calls the function Mouth() to draw their mouths and the
#function Antenna() to draw their anttenas.

from graphics import *
from random import*


def main():
        #define the object windows canvas
	win = GraphWin('Aliens', 500,500)
	win.setBackground("lightcoral")
	win.setCoords(-100,-100,100,100)

	#set the initial value of the scale to 3
	scale = 3
	
    #draw 30 Aliens by calling the function AlienHead() 20 times
	for i in range (0,50):
        #Get random number from (-100,100) for the values of x and y
        #(x,y) is the center point of the alien's face
		x = randint(-100,100)
		y = randint(-100,100)
		AlienHead(x,y,scale,win)
		#increase the scale by 0.08 at every end of the loop
		scale = scale+0.08
		
	drawText(win)

	while True:
		if win.getMouse():
			win.close()

def AlienHead(x,y,scale,win):
	'''(x,y,scale,win),draws the Alien's head
	'''
	Antenna(x,y+3.5*scale,scale,win)
	head = Oval(Point(x-5.5*scale,y-3.5*scale),Point(x+5.5*scale,y+3.5*scale))
	head.setFill("yellowgreen")
	head.draw(win)
        #Call the Mouth() function inside Alienhead() function
	Mouth(x,y,scale,win)
	#Call the Eyes function inside the Alienhead() function,
	Eyes(x-2.5*scale,y+scale,scale,win)
	Eyes(x+2.5*scale,y+scale,scale,win)
	Eyes(x,y+1.8*scale,scale,win)
	
	
def drawText(win):
	#draw a text at the center of the canvas
	text = Text(Point(0,0), "Hello my friend")
	text.setSize(36)
	text.setTextColor("purple")
	text.setStyle("bold")
	text.draw(win)

	text = Text(Point(0,-15), "Click to quit")
	text.setSize(24)
	text.setTextColor("pink")
	text.setStyle("bold")
	text.draw(win)



def Mouth(x,y,scale,win):
	'''(x,y,scale,win),draws the Alien's mouth
	'''
	mouth = Polygon(Point(x-4*scale,y-0.5*scale),
			Point(x-3*scale,y-scale),
			Point(x+3*scale,y-scale),
			Point(x+4*scale,y-0.5*scale),
			Point(x+3*scale,y-scale),
			Point(x,y-2.5*scale),
			Point(x-3*scale,y-scale),
			Point(x-4*scale,y-0.5*scale))
	mouth.setFill("indianred")
	mouth.draw(win)
	
def Eyes(x,y,scale,win):
	'''(x,y,scale,win),draws the Alien's eye
	'''
	eye = Circle(Point(x,y),scale)
	eye.setFill("white")
	eye.draw(win)
	pupil = Circle(Point(x,y-scale/3),0.25*scale)
	pupil.setFill("black")
	pupil.draw(win)

def Antenna(x,y,scale,win):
        antenna=Rectangle(Point(x-0.2*scale,y),
                          Point(x+0.2*scale,y+2.5*scale))
        antenna.setFill("olivedrab2")
        antenna.draw(win)
        antennatop=Circle(Point(x,y+2.5*scale),0.3*scale)
        antennatop.setFill("olivedrab2")
        antennatop.draw(win)

 


main()


