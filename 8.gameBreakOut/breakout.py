# Yining Hua
# Breakout.py

# Notes:
# In this game, the horizontal speed x is used for controlling direction
# the vertical speed y is used to adjust falling speed.
#
# Some added features: 
# 1.You can select hardlevel before start the games.
# 2.You have 3 lifes. If you miss the paddle for 3 times, game over.

from graphics import *
from random import randint,uniform
from time import sleep
    
def main():
    '''Breakout
    '''
    # Set up window
    win = Windows(100)
    # Create objects
    paddle = Paddle(win)
    ball1 = Ball(win,randint(-96,96),96,'gray')
    point = 0
    oldpoint,newpoint = PointGraph(win,point)
    misstime = 0
    w = 100
    #draw the bricks
    brick1 = Brick(win,-80,60,'red','pink')
    brick2 = Brick(win,-40,60,'red','pink')
    brick3 = Brick(win,0,60,'red','pink')
    brick4 = Brick(win,40,60,'red','pink')
    brick5 = Brick(win,80,60,'red','pink')
    bricks = [brick1,brick2,brick3,brick4,brick5]
    #Get the hardlevel the player wants
    print("Welcome to Breakout!\rYou have 3 chances to lose the ball each turn.\nWithin each turn, everytime you miss the ball you'll have 2 seconds pause.\n")
    hardlevel = eval(input("Choose hard level(easy = 1,normal = 2, hard = 3): "))
    #The speed is decided by the hard level the player chose
    dx,dy = Randvelocity(),hardlevel*0.5
    print("Selected. Click on the window to start game.")

    win.getMouse()
    while True:
        key = win.checkKey()
        #if player presses the period key:: break
        if (key == 'period') :
            break
        #if player misses the ball for 3 times:: game over
        elif(misstime == 3):
            Lose(win,misstime)
            break
        #else:: play game 
        else:
            Paddlemove(paddle,w,key)
            ball1.move(dx,dy);
            if not CircInWindow( ball1, w-4, paddle):
                dx,dy,point,misstime = ReflectCirc(ball1,dx,dy,w-4,paddle,point,misstime,bricks,win)
        
        
    # update( 10000 )
    win.getMouse( )
    win.close( )



#========================Helper===Functions===========================

def Randvelocity():
    '''This function creates random velocity between (-1.5,-.8)&(.8,1.5)
    '''
    a,b = uniform(-1.5,-.8),uniform(.8,1.5)
    l = [a,b]
    v = l[randint(0,1)]
    return v

def Windows(w):
    '''Windows(w)::creates a window
    '''
    win = GraphWin( 'Break Out', 500, 500, autoflush = False)
    win.setBackground("black")
    win.setCoords( -w, -w, w, w )
    return win;

def Ball(win,x,y,color):
    '''Ball(win,x,y,color)::draws the ball
    '''
    print('Ball')
    circ = Circle( Point(x,y), 4 )
    circ.setFill( color )
    circ.draw( win )
    return circ;

def Brick(win,x,y,coloutline,colsetfill):
    '''Brick(win,x,y,coloutline,colsetfill)::Draws a brick with given features
    '''
    print("brick")
    rect = Rectangle(Point(x-19,y-1.5),Point(x+19,y+1.5))
    rect.setOutline(coloutline)
    rect.setFill(colsetfill)
    rect.draw(win)
    return rect

def Paddle(win):
    '''Paddle(win)::creates a paddle
    '''
    print("paddle")
    rect = Rectangle(Point(-13,-87),Point(13,-83))
    rect.setFill("pink")
    rect.setOutline('red')
    rect.draw(win)
    return rect;

def Paddlemove(paddle,w,key):
    '''Paddlemove(paddle,w):: Make the paddle move within the window
    '''
    paddlec = paddle.getCenter()
    paddlex = paddlec.getX()

    if (-w<(paddlex-18)) and ((paddlex+18)<w):
        if key == 'Left':
            paddle.move(-8,0)
        if key =='Right':
            paddle.move(8,0)
    elif (-w>=(paddlex-18)):
        if key =='Right':
            paddle.move(8,0)
    elif ((paddlex+18)>=w):
        if key == 'Left':
            paddle.move(-8,0)


def MoveCircTo( circ, xnew,ynew ):
    '''Move the circle object to new coords
    '''
    # Extract the circle data:
    pcent = circ.getCenter( )
    xc,yc = pcent.getX(), pcent.getY()

    # Compute displacement
    dx = xnew - xc
    dy = ynew - yc

    circ.move( dx, dy )

def CircInWindow( circ, w , paddle ):
    '''CircInWindow( circ, w , paddle):: Check if the ball hits the wall or the paddle. 
    '''
    # Extract the circle data:
    paddlec = paddle.getCenter()
    paddlex,paddley = paddlec.getX(),paddlec.getY()
    pcent = circ.getCenter( )
    xc,yc = pcent.getX(), pcent.getY()

    # In the window if in horiz & vert
    if (yc <= -79) and (paddlex - 13 <= xc <= paddlex +13):
        return False
    elif(55<=yc<=(65)):
        return False
    elif (-w <= xc <= w) and (-w <= yc <= w):
        return True
    else:
        return False

def ReflectCirc(circ,dx,dy,w,paddle,point,misstime,bricks,win):
    '''
    ReflectCirc( circ, dx,dy, w ,paddle,point,misstime)::
    Reflect the ball when it hits the walls or paddle.
    If the ball hits the paddle, add one point;
    If misses, add misstime by one.
    Return the new move elements, point variable, misstime variable.
    '''
    # Extract the circle data:
    pcent = circ.getCenter( )
    xc,yc = pcent.getX(), pcent.getY()
    paddlec = paddle.getCenter()
    paddlex,paddley = paddlec.getX(),paddlec.getY()
    # Initialize in case no change
    xnew,ynew = xc,yc
    dxnew,dynew = dx,dy
   
    # Reflect x, horiz:
    if xc > w:
        xnew = w
        dxnew = -dx
    elif xc < -w:
        xnew = -w
        dxnew = -dx


    # Reflect y, vert
    #If hits the upper wall
    if yc > w:
        #Currently commentes out, this line put the ball at a random x-axis place
        #xnew = randint(-96,96)
        ynew = w
        #the speed becomes 1.2 times faster than original speed
        dxnew = uniform(-1,1)
        dynew = -(dy+0.5)

    #if the ball comes to the bottom
    elif yc<-w:
        #starts at a random point at the top
        xnew = randint(-96,96)
        ynew = 96
        #at the same spped as the initial speed
        dxnew,dynew = dx,dy
        #If miss, the animation stops for 2 seconds
        misstime+=1
        sleep(2)

    elif (55<=yc<=65):
        y = 60
        if (-100<=xc<=-60):
            bricks[0].undraw()
        elif (-60<=xc<=-20):
            bricks[1].undraw()
        elif (-20<=xc<=20):
            bricks[2].undraw()
        elif (20<=xc<=60):
            bricks[3].undraw()
        elif (60<=xc<=100):
            bricks[4].undraw()
        #if breaks a brick, point+1

    #if the ball hits the paddle
    elif (yc <= -79) and (paddlex-17 <= xc <= paddlex + 17):
        #If the ball is inside the paddle, move the ball out of the paddle first.
        ynew = -79.1
        #ball bounces back
        dynew = -dy
        #Add 1 to the total points when the ball hits the paddle
        point = point+1
        #Draw the point on the screen
        PointGraph(win,point)

    #Move the ball to a new place with new speed
    MoveCircTo( circ, xnew,ynew )

    # Return the new drift speeds:
    return dxnew,dynew, point ,misstime  
    
def PointGraph(win,point):
    '''PointGraph(win,point):: returns the graph objects of points the player gets in the game
    '''
    textold = Text(Point(85,85),(point-1))
    textold.setFill("black")
    textold.setSize(20)
    textold.draw(win);

    textnew = Text(Point(85,85),point)
    textnew.setFill("red")
    textnew.setSize(20)
    textnew.draw(win);

    return textold,textnew

def Lose(win,misstime):
    '''Lose(win,misstime)::Print out 'GAME OVER' when you miss 3 times
    '''
    text = Text(Point(0,0),"GAME OVER")
    text.setFill("darkred")
    text.setSize(28)
    text.draw(win)

main()
