#Mondrian.py
#Sarah Knoblach and Yining Hua
#Lab 10
#Creates a Mondrian like painting(??), 
#expresses the extreme uncertainty and anxiety of the artist

from graphics import *
from random import randint, uniform 

def main():
    # Set up window
    w=100 #Sets the variable
    win = createWindows(w)
    sq = createSquare(win,w)
    depth=0
    PaintPartition(win,sq,depth)

    win.getMouse( )
    win.close( )

def createSquare(win,w):
    p1=Point(-w,w)
    p2=Point(w,-w)
    sq=Rectangle(p1,p2)
    return sq

def createWindows(w):
    win=GraphWin('Mondrian', 500, 500)
    win.setCoords(-w,-w,w,w)
    return win

def PaintPartition( win, sq, depth ):
    dmax=4
    if depth > dmax:
        return
    colors=['pink2','pink','gray','gray2','pink1']
    i=randint(0,len(colors)-1)
    sq.setFill(colors[i])
    sq.draw(win)
    # Decide whether or not to recurse
    x=randint(1,20)
    if x <= 1: # 5% of the time
        # Do not recurse:
        return
    # Now have decided to recurse (95% of the time)
    # Create four quadrant sub-squares
    Lsquares=getQuadrants(sq)
    # (4)
    # Recurse of four sub-squares:
    for square in Lsquares:
        PaintPartition( win, square, depth + 1 )   
    #get the list of four quadrants

def getQuadrants(sq):
    '''getQuadrants(sq)::= Divides the larger square into smaller squares
    '''

    p1=sq.getP1()
    p2=sq.getP2()    
    p3=Point(p1.getX(),p2.getY())
    p4=Point(p2.getX(),p1.getY())
    #A random point inside the rectangle
    p5=Point(uniform(p1.getX(),p2.getX()),uniform(p2.getY(),p1.getY()))

    #divide a bigger rectangle into 4 smaller ones
    rect0=Rectangle(p2,p5)
    rect1=Rectangle(p5,p3)
    rect2=Rectangle(p5,p1)
    rect3=Rectangle(p5,p4)

    Lrect=[rect0,rect1,rect2,rect3]
    return Lrect
    
main()
