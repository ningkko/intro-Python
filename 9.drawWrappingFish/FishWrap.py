# Lab 9
# Jacqueline Richardson & Yining Hua
# A program that draws fish in the window

from graphics import *
from random import randint,uniform

def CreateFish(win,position, size):
    
    L=30 * size

    tail = Oval(Point(position.getX()+L/3,position.getY()-L/4),Point(position.getX()+L/3,position.getY()+L/4))
    tail.setFill("LightCoral"))
    tail.draw(win)

    body = Oval(Point(position.getX()-L/2,position.getY()-L/4),Point(position.getX()+L/2,position.getY()+L/4))
    body.setFill("LightCoral")
    body.draw(win)

    eye = Circle(Point(position.getX()-L/4,position.getY()),L/15)
    eye.setFill("white")
    eye.draw(win)




    return  [tail,body,eye];

def PtInRect( p, rect ):
    '''Is point p in the rectangle?
    '''
    # Extract the pt coords:
    xp,yp = p.getX(),p.getY()

    # Extract the rect corners:
    p1 = rect.getP1()
    x1,y1 = p1.getX(),p1.getY()
    p2 = rect.getP2()
    x2,y2 = p2.getX(),p2.getY()
    # Assume p1 is lower-left, p2 upper-right

    # In the rect when between both x&y:
    if (x1 <= xp <= x2) and (y1 <= yp <= y2):
        return True
    else:
        return False

def MoveCircTo( circ, xnew,ynew ):
    '''Move the circle object tp new coords
    '''
    # Extract the circle data:
    pcent = circ.getCenter( )
    xc,yc = pcent.getX(), pcent.getY()

    # Compute displacement
    dx = xnew - xc
    dy = ynew - yc

    circ.move( dx, dy )

    
def WrapCirc( circ, w ):
    '''Wrap the coords if outside +/w
       Move circ to wrapped coords.
    '''
    # Extract the circle data:
    pcent = circ.getCenter( )
    xc,yc = pcent.getX(), pcent.getY()

    xnew,ynew = xc,yc

    # Wrap x, horiz:
    if xc > w:
        xnew = xc - 2*w
    elif xc < -w:
        xnew = xc + 2*w

    # Wrap y, vertical
    if yc > w:
        ynew = yc - 2*w
    elif yc < -w:
        ynew = yc + 2*w

    MoveCircTo( circ, xnew,ynew )       

def main():
    '''Click disk game'''
    # Set up window
    win = GraphWin( 'Click Disk', 500, 500,autoflush = False)
    win.setBackground( 'LightSteelBlue' )
    w = 100
    win.setCoords( -w, -w, w, w )

    # Create objects
    r = 10
    p1 = Point( 90,90 )
    p2 = Point( 100,100 )
    sq = Rectangle( p1, p2 )
    sq.setFill( 'pink' )
    sq.draw( win )


    lfish = []
    for i in range (10):
        lfish.append(CreateFish(win,Point(uniform(-100,100),uniform(-100,100)),uniform(0.8,1.3)))
        
    
    #---------------
    # Animation loop
    dx,dy = -2,0
    
    while True:
        p = win.checkMouse( )
        if p: # if user clicked
            if PtInRect( p, sq ):
                print( 'Click is inside square' )
                break
                
        
        for n in range(10):
            lfish[n][0].move(dx,dy)
            lfish[n][1].move(dx,dy)
            lfish[n][2].move(dx,dy)
            WrapCirc( lfish[n][0], w )
            WrapCirc( lfish[n][1], w )
            WrapCirc( lfish[n][2], w )
        
    update(10000)
        
                
    #---------------
    # Wait for click
    update()
    win.getMouse( )
    win.close( )

main()
