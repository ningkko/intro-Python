# Yining Hua
# Lab8: User walks through a maze.
# Maze code provided by JORourke

from random import shuffle, randrange
from graphics import *

#================================================================
def MakeStringMaze(w = 12, h = 8):
    ''' https://rosettacode.org/wiki/Maze_generation#Python
        (Author unknown, but based on
        https://en.wikipedia.org/wiki/Maze_generation_algorithm.)
        Default w,h=12,8. Returns a string.
    '''
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)
 
    walk(randrange(w), randrange(h))

    # Create a string representation of the maze:
    s = ''
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s

def DrawMaze( s, win, w ):
    '''Convert string-maze s to graphics-maze.
       Assumes default w,h=12,8, and win coords +/-100.
       Author: JORourke
    '''
    # Break up s into rows:
    slist = s.split( '\n' )

    dx,dy = 5,10 # Mimic char aspect ratio, about 1::2
    Lgobjs=[] # List of graphics objects
    # i : controls x coord
    # j : controls y coord
    for j in range( len( slist ) ):
        row = slist[j]
        y = -j * dy + w - 2*dy
        for i in range( len(row) ):
            x = i * dx - w + 2*dx
            c = row[i] # c: single character
            if c=='|':
                Lgobjs.append( Line(Point(x,y+dy),Point(x,y-dy)) )
            elif c=='-':
                Lgobjs.append( Line(Point(x-dx,y),Point(x+dx,y)) )

    # Now draw all the graphic objects                              
    for gobj in Lgobjs:
        gobj.setWidth( 2 )
        gobj.setFill( 'DarkBlue' )
        gobj.draw( win )

    # Begin & End circs
    def BeginEnd( x, y ):
        print( 'Corner:', x, y)
        p = Point( x, y )
        circ = Circle( p, dx )
        circ.setFill( 'Pink' )
        circ.draw( win )

    BeginEnd( x, y+2*dy )
    BeginEnd( -w + dy, w - 2*dy )
#================================================================


def main( ):
    win = GraphWin( 'Maze', 500, 500 )
    win.setBackground( 'cornflowerblue' )
    w = 100
    win.setCoords( -w, -w, w, w)

    # Create a maze as a string:
    s = MakeStringMaze( )
    print( s )
    # Convert string maze to graphics maze:
    DrawMaze( s, win, w )


    #-----------------------------------------

    token = drawtoken(win);
        
    # get the key
    k = win.getMouse();
    print("Now: checkKey()[focus in window]...");
    while True:
        k = win.checkKey()
        p1 = token.getCenter()

        if (k!= ''):
            print('k =',k)
            print(token.getCenter())

        if (k == 'period'): break;

        tokenmove(k,token);
        p2 = token.getCenter()
        line = drawline(win,p1,p2);
        if (p2.getX()==-90) and (p2.getY()==80):
            youWin(win)
            break

#-----------------------------------------

    print( 'Click in window to close' )
    win.getMouse( )
    win.close( )



def drawtoken(win):
    circle = Circle(Point(90,-80),5)
    circle.setFill("pink")
    circle.draw(win)
    return circle;
    
def tokenmove(direction,token):
    if direction == 'Left':
        token.move(-4,0)
    elif direction == 'Up':
        token.move(0,4)
    elif direction== 'Down':
        token.move(0,-4)
    elif direction =='Right':
        token.move(4,0)

def drawline(win,p1,p2):
    line = Line(p1,p2)
    line.setFill('yellow')
    line.setWidth(2)
    line.draw(win)
    return line;

def youWin(win):
    print("Brava!");
    AlienHead(0,0,10,win)
    text = Text(Point(0,0),"BRAVA!")
    text.setFill("purple")
    text.setSize(24)
    text.draw(win);

def AlienHead(x,y,scale,win):
    '''(x,y,scale,win),draws the Alien's head
    '''
    Antenna(x,y+3.5*scale,scale,win)
    head = Oval(Point(x-5.5*scale,y-3.5*scale),Point(x+5.5*scale,y+3.5*scale))
    head.setFill("pink")
    head.draw(win)
        #Call the Mouth() function inside Alienhead() function
    Mouth(x,y,scale,win)
    #Call the Eyes function inside the Alienhead() function,
    Eyes(x-2.5*scale,y+scale,scale,win)
    Eyes(x+2.5*scale,y+scale,scale,win)
    Eyes(x,y+1.8*scale,scale,win)
    
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
        antenna.setFill("pink")
        antenna.draw(win)
        antennatop=Circle(Point(x,y+2.5*scale),0.3*scale)
        antennatop.setFill("pink")
        antennatop.draw(win)


main()
