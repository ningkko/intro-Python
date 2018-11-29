# Assignment 9
# Yining Hua
# A program that draws an aquarium

from graphics import *
from random import randint,uniform

def main():
    '''An aquarium'''

    #Create objects
    win = createWindows()
    sq = createExit(win)

    catPupil1,catPupil2 = cat(win)
    lbubble = createBubbles(win)
    createGrass(win)
    createStones(win)
    lfish = createFish(win)
    seaWeed(-50,-2,win)

    #For counting the frames
    frame = 0

    #Animation loop
    while True:

        frame += 1

        #If click inside the square, break
        if checkExit(win,sq): break

        #Move the cat's pupils
        catMovePupil(catPupil1,catPupil2,frame)
        #Movd the fish and bubbles   
        moveWithBobbing(win,frame,lfish,lbubble)

    update(10)
        
    #---------------
    # Wait for click
    win.getMouse( )
    win.close( )

#=========== Classes ====================

class Bubbles:

    def __init__(self,win):
        '''Bubble constructor
        '''
        bubble = Circle(Point(randint(-100,100),randint(-75,100)),2)
        bubble.setFill("white")
        bubble.draw(win)
        self.bubble = bubble
        self.yspeed = uniform( 1.3, 1.8 )

    def moveBubble(self,direction):
        '''Moves the bubble'''
        self.bubble.move(2*direction,self.yspeed)

    def wrapBubble(self,w):
        '''wraps the bubble
        '''
        wrapCirc(self.bubble,w)

class Fish:

    def __init__(self,win,position,direction):
        #Scale of the fish
        L=17
        
        #Some pink colors
        #colorsets = ["lightpink","lightpink1","lightpink2","lightpink3","hotpink","pink","pink2","pink3","hotpink1","palevioletred","palevioletred1","palevioletred2","palevioletred3","hotpink2","hotpink3"]
        colorsets = ["gray90","gray83","gray85","gray80","gray77","gray75","gray70","gray65","gray63","gray60","gray55","gray50"]
        randomcolor = colorsets[randint(0,11)]
        tail = Oval(Point(position.getX()-L/3.5*direction,position.getY()-L/1.5),Point(position.getX()-L/2*direction,position.getY()+L/1.5))
        tail.setFill(randomcolor)
        tail.draw(win)

        body = Oval(Point(position.getX()-L/1.6,position.getY()-L/3),Point(position.getX()+L/1.6,position.getY()+L/3))
        body.setFill(randomcolor)
        body.draw(win)

        eye = Circle(Point(position.getX()+L/3*direction,position.getY()+L/7),L/23)
        eye.setFill("white")
        eye.draw(win)

        #self. reserves information for future use after costruction
        self.parts = [tail,body,eye]

        #store speed variables
        self.xspeed = uniform( 0.5,3 )*direction
        #do not need to return because this's a constructor


    # def getFishCenter(self):
    #     point = self.parts[2].getCenter()
    #     return point

    def moveFish(self,direction):
        for obj in self.parts:
            obj.move(self.xspeed,2*direction)

    def wrapFish(self,w):
        for obj in self.parts:
            wrapCirc(obj,w)

#=========== Create Functions ===========

def seaWeed(a,b,win):
    grass = Polygon(Point(a,b),
            Point((a+5),(b-90)),
            Point((a+8),(b+7)),
            Point((a+11),(b-90)),
            Point((a+16),(b)),
            Point((a+15),(b-96)),
            Point((a+1),(b-96)),
            Point(a,b))
    grass.setFill(color_rgb(100, 145, 36))
    grass.setOutline("")
    grass.draw(win)

def createStones(win):
    '''creates stones, and some seaweeds.
    '''

    def stone(win,size,position):
        L = 10*size
        stone = Oval(Point(position.getX()-L/1.6,position.getY()-L/2),Point(position.getX()+L/1.6,position.getY()+L/2.5))
        stone.setFill('ivory3')
        stone.draw(win)

    seaweed1 = seaWeed(-95,20,win)
    stone13 = stone(win,3,Point(-50,-70))
    stone4 = stone(win,2.2,Point(-70,-80))
    stone3 = stone(win,1.5,Point(-80,-85))
    stone1 = stone(win,3,Point(-100,-80))
    stone2 = stone(win,1,Point(-90,-90))
    stone5 = stone(win,0.8,Point(-55,-92))
    stone6 = stone(win,1.5,Point(-25,-75))
    stone7 = stone(win,1.8,Point(-35,-85))
    stone8 = stone(win,1.3,Point(-10,-85))
    stone9 = stone(win,1.8,Point(10,-85))
    stone10 = stone(win,1,Point(20,-90))
    seaweed3 = seaWeed(-30,0,win)
    stone12 = stone(win,2.5,Point(50,-70))
    stone11 = stone(win,1.8,Point(35,-80))
    seaweed4 = seaWeed(40,5,win)
    stone14 = stone(win,1,Point(50,-93))
    seaWeed(87,22,win)
    stone16 = stone(win,2,Point(80,-80))
    stone15 = stone(win,1.5,Point(72,-85))
    stone16 = stone(win,3,Point(100,-95))

def createGrass(win):
    '''createGrass(win)::=
    Creates different types of grasses.
    '''

    #part1: grassland
    color = "darkolivegreen"
    grassland = Rectangle(Point(-100,-110),Point(105,-72))
    grassland.setFill(color)
    grassland.setOutline("")
    grassland.draw(win)

    #part2: grassland upper
    def grass2(win,x,y):
        grass = Text(Point(x,y),"*")
        grass.setFill(color)
        grass.setSize(24)
        grass.draw(win);
    for i in range (-100,100,2):
           grass2(win,i,-74)

    #part3: specific grass
    def grass(a,b,win):
        grass = Polygon(Point(a,b),
                Point((a+5),(b-8)),
                Point((a+8),(b+1)),
                Point((a+11),(b-8)),
                Point((a+16),(b+1)),
                Point((a+15),(b-12)),
                Point((a+1),(b-12)),
                Point(a,b))
        grass.setFill(color_rgb(100, 145, 36))
        grass.setOutline("")
        grass.draw(win)

    for m in range(0,30):
        grass(randint(-100,100),randint(-100,-65),win)

def createWindows():
    '''CreateWindows()::= 
    sets up the window.
    '''

    win = GraphWin( 'Fishes', 500, 500,autoflush = False)
    win.setBackground( 'lightskyblue3' )
    w = 100
    win.setCoords( -w, -w, w, w )
    return win

def createExit(win):
    '''CreateExit(win)::= 
    Creats the exit buttom.
    '''
    p1,p2 = Point( 90,90 ) ,Point( 100,100 )
    sq = Rectangle( p1, p2 )
    sq.setFill( 'pink' )
    sq.draw( win )
    return sq

def createBubbles(win):
    '''CreateBubbles(win)::= 
    Create bubbles.
    '''
    lbubble = []
    for i in range (30):
        lbubble.append(Bubbles(win))
    return lbubble

def createFish(win):
    '''CreateFish(win)::= 
    Creates fish.
    '''
    lfish = []
    ldirection = [1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1]
    for i in range (16):
        lfish.append(Fish(win,Point(uniform(-100,100),uniform(-80,100)),ldirection[i]))
    return lfish

def cat(win):
    '''cat(win)::= 
    A revised version of a former assignment. 
    Draws the cat, returns the 2 pupils.
    '''
    def catPaw(x,y,scale,win):
        '''(x,y,scale,win),draws the Alien's eye
        '''
        paw1 = Oval(Point(x-5.5*scale,y-4.5*scale),Point(x+5.5*scale,y+4.5*scale))
        paw1.setFill("white")
        paw1.draw(win)
        paw2(x-2.5*scale,y+scale,scale,win)
        paw2(x+2.5*scale,y+scale,scale,win)
        paw2(x,y+1.8*scale,scale,win)
        paw3= Oval(Point(x-2.5*scale,y-2.5*scale),Point(x+2.5*scale,y+0.2*scale))
        paw3.setFill("pink2")
        paw3.draw(win)

    def paw2(x,y,scale,win):
        paw = Circle(Point(x,y),scale)
        paw.setFill("pink2")
        paw.draw(win)

    catPaw(-78,-15,3.8,win)
    catPaw(78,-15,3.8,win)


    catE1 = Polygon(Point(-65,90),Point(-55,0),Point(-10,70))
    catE1.setFill("pink2")
    catE2 = Polygon(Point(65,90),Point(55,0),Point(10,70))
    catE2.setFill("pink2")

    catFace = Oval(Point(-70,-35), Point(70,80))
    catFace.setFill("lavenderblush")

    catEye1 = Circle(Point(-35,35), 10)
    catEye1.setFill("yellow")
    catEye2 = Circle(Point(35,35),10)
    catEye2.setFill("yellow")

    catPupil1 = Circle(Point(-35,30),5)
    catPupil1.setFill("black")
    catPupil2 = Circle(Point(35,30),5)
    catPupil2.setFill("black")

    catNose = Polygon(Point(-10,13),Point(0,7),Point(10,13))
    catNose.setFill("pink2")

    catMouse = Polygon(Point(-5,-1),Point(0,7),Point(5,-1))
    catMouse.setFill("indianred")

    catE1.draw(win)
    catE2.draw(win)
    catFace.draw(win)
    catEye1.draw(win)
    catEye2.draw(win)
    catPupil1.draw(win)
    catPupil2.draw(win)
    catNose.draw(win)
    catMouse.draw(win)

    return catPupil1,catPupil2

#=========== Method Functions ============
def catMovePupil(catPupil1,catPupil2,frame):
    '''catMovePupil(catPupil1,catPupil2,frame)::= Moves the pupils regarding to the frame counts
    '''
    #Move upwards
    for i in range(20,60,1):
        if (frame%300 == i):
            catPupil1.move(0,.25)
            catPupil2.move(0,.25)
    #Move downwards
    for j in range(170,210,1):
        if(frame%300 == j):
            catPupil1.move(0,-.25)
            catPupil2.move(0,-.25)

def checkExit(win,sq):
    '''checkExit(win)::= checks whether the click inside the exit buttom
        return True if click is inside
    '''
    p = win.checkMouse( )
    if p: # if user clicked
        if PtInRect( p, sq ):
            print( 'Click is inside square' )
            return True   

def MoveCircTo( circ, xnew,ynew ):
    '''MoveCircTo( circ, xnew,ynew )::= moves the circle object to new coords
    '''
    # Extract the circle data:
    pcent = circ.getCenter( )
    xc,yc = pcent.getX(), pcent.getY()

    # Compute displacement
    dx = xnew - xc
    dy = ynew - yc

    circ.move( dx, dy )

def moveWithBobbing(win,frame,lfish,lbubble):  
    #======================Fish=====================
    #devide the fish into 4 groups for bobbing at 4 different rates
    for i in range (0,4,1):
        if (frame%30 == 0):
            lfish[i].moveFish(1)
            lfish[i].wrapFish(100)
        if (frame%30 == 15):
            lfish[i].moveFish(-1)
            lfish[i].wrapFish(100)

    for i in range (4,8,1):
        if (frame%50 == 0):
            lfish[i].moveFish(1)
            lfish[i].wrapFish(100)
        if (frame%50 == 25):
            lfish[i].moveFish(-1)
            lfish[i].wrapFish(100)

    for i in range (8,12,1):
        if (frame%36 == 0):
            lfish[i].moveFish(1)
            lfish[i].wrapFish(100)
        if (frame%36 == 18):
            lfish[i].moveFish(-1)
            lfish[i].wrapFish(100)

    for i in range (12,16,1):
        if (frame%24 == 0):
            lfish[i].moveFish(1)
            lfish[i].wrapFish(100)
        if (frame%24 == 12):
            lfish[i].moveFish(-1)
            lfish[i].wrapFish(100)

    #===================Bubbles====================
    
    #devide the bubbles into 3 groups for shaking at 3 different rates
    i = 0
    for i in range (0,10,1):
        if (frame%15 == 0):
            lbubble[i].moveBubble(-1)
            lbubble[i].wrapBubble(100)
        if (frame%15 == 5):
            lbubble[i].moveBubble(1)
            lbubble[i].wrapBubble(100)

    for i in range (10,20,1):
        if (frame%10 == 0):
            lbubble[i].moveBubble(-1)
            lbubble[i].wrapBubble(100)
        if (frame%10 == 5):
            lbubble[i].moveBubble(1)
            lbubble[i].wrapBubble(100)

    for i in range (20,30,1):
        if (frame%30 == 0):
            lbubble[i].moveBubble(-1)
            lbubble[i].wrapBubble(100)
        if (frame%30 == 15):
            lbubble[i].moveBubble(1)
            lbubble[i].wrapBubble(100)

    #else, just move straightly
    else:
        for m in range(30):
            lbubble[m].moveBubble(0)
            lbubble[m].wrapBubble(100)
        for n in range(16):
            lfish[n].moveFish(0)
            lfish[n].wrapFish(100)

def PtInRect( p, rect ):
    '''PtInRect( p, rect )::= Checks wether the mouse clicks in a rectangle
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

def wrapCirc( circ, w ):
    '''WrapCirc( circ, w )::= Wraps the coords if outside +/w. Moves circ to wrapped coords
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




main()
