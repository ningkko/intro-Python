#Yining Hua
#Pumkin.py = HW#3
#A program draws a horrible scene of a weird night
#which has randomly moving stars and grass


from graphics import *
from random import*

def main():
	#creat the object
	win = GraphWin('Pumpkin', 500,500)
	#set the background to be the color of night
	win.setBackground("darkblue")
	win.setCoords(-100,-100,100,100)

	#draw the grassland
	grassland = Rectangle(Point(-120,-15), Point(120,-200))
	grassland.setFill("darkgreen")
	grassland.draw(win)

#we're now in thesky
	
	#draw the random stars
	for n in range (0,50):
			star = Circle(Point(randint(-200,200),randint(0,100)),0.8)
			star.setFill("white")
			star.draw(win)		

	#draw the special star
	starSC1 = Circle(Point(70,80),4)
	starSC1.setFill("white")
	starSC1.draw(win)
	starSC2 = Circle(Point(66,84),4.2)
	starSC2.setFill("darkblue")
	starSC2.setOutline("")
	starSC2.draw(win)
	starSC3 = Circle(Point(74,84),4.2)
	starSC3.setFill("darkblue")
	starSC3.draw(win)
	starSC3.setOutline("")
	starSC4 = Circle(Point(66,76),4.2)
	starSC4.setFill("darkblue")
	starSC4.draw(win)
	starSC4.setOutline("")
	starSC5 = Circle(Point(74,76),4.2)
	starSC5.setFill("darkblue")
	starSC5.draw(win)
	starSC5.setOutline("")

	#draw the moon
	moonouter = Circle(Point(-65,65),25)
	moonouter.setFill("yellow")
	moonouter.draw(win)
	mooninner = Circle(Point(-58,70),23)
	mooninner.setFill("darkblue")
	mooninner.setOutline("")
	mooninner.draw(win)

#Now we come to the land
	
	#a function for drawing grass
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
		
	#call the function to draw 60 sets of grass(doubled y
        #space for generating a more even result)
	for m in range(0,60):
		grass(randint(-100,100),randint(-200,-5),win)


	
	#A list of x locations for pumpkins
	placex = [-50, -30,-102, 60, 99, 23, -54, 77, 40,-29,-90]
	#A list of y locations for pumpkins
	placey = [-15, -20,-33,-30,-28,-60,-66,-70,-75,-80,-90]
        #Let n = the initialvalkue of pumpkin radius        
	n = 12
	#Draw ten pumpkins
	for i in range (0,11):
                #pumpkin bodies
		pumpkin1 = Circle(Point(placex[i]-n/3,placey[i]),n-1)
		pumpkin1.setFill(color_rgb(165, 53, 13))
		pumpkin1.draw(win)
		
		pumpkin2 = Circle(Point(placex[i]+n/3,placey[i]),n-1)
		pumpkin2.setFill(color_rgb(165, 53, 13))
		pumpkin2.draw(win)

		#draw stems
		stem = Polygon(Point(placex[i]-n/13, placey[i]+n-3),
				Point(placex[i]+n/10, placey[i]+n+n/3),
				Point(placex[i]+n/5, placey[i]+n+n/3.2),
				Point(placex[i]+n/13, placey[i]+n-5))
		stem.setFill(color_rgb(8,102,36))
		stem.draw(win)
		pumpkin3 = Circle(Point(placex[i],placey[i]-n/18),n*12/13)
		pumpkin3.setFill(color_rgb(165, 53, 13))
		pumpkin3.draw(win)
		#Increase n by 1 at every end of the loop (to show distance)
		n = n+1
		
	#Draw face of the Jack-o'lantern	
	JakeE1 = Polygon(Point(46,-71),Point(50,-63),Point(56,-71))
	JakeE1.setFill(color_rgb(255,227,20))
	JakeE1.draw(win)
	JakeE2 = Polygon(Point(34,-71),Point(29,-63),Point(24,-71))
	JakeE2.setFill(color_rgb(255,227,20))
	JakeE2.draw(win)
	
	JakeNose = Polygon(Point(40,-69),Point(36,-78),Point(44,-78))
	JakeNose.setFill(color_rgb(255, 227, 20))
	JakeNose.draw(win)

	JakeMouth = Polygon(Point(23,-76),
			    Point(31,-82),
			    Point(31,-84),
			    Point(35,-84),
			    Point(35,-82),
			    Point(45,-82),
			    Point(45,-84),
			    Point(49,-84),
			    Point(49,-82),
			    Point(57,-76),
			    Point(52,-85),
			    Point(47,-87),
			    Point(34,-87),
			    Point(28,-84),
			    Point(23,-76))
	JakeMouth.setFill(color_rgb(255,227,20))
	JakeMouth.draw(win)

#we're done.
			
	win.getMouse()
	win.close()
		
main()

