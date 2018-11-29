#Sea.py
#Yining Hua
#Assignment 1
#Produces a table and chart of sea level rise

def main():
    #get datas from users by using function input(); convert them into num-type datas by using eval()
    rate = eval(input("enter rate(mm/yr):"));
    accel = eval(input("enter accel(mm/yr):"));
    year = eval(input("enter # of years(at most 9):"));
    level = 0.0;
    #create temporary variables for the first for loop
    r = rate;
    l = level;
    #create a temporary variable n for changing years.
    #for the year within [0 , the last year], loop the function and add the year by 1)
    for n in range(0,year+1,+1):
        #print out the data in year n
        print("after year ",round(n,1)," rate= ",round(r,1)," level= ",round(l,1)," mm");
        #make changes to the sea level and the rate at every end of a year.
        l = l + r;
        r = r + accel;
    #from year 0 to year max    
    for n in range(0,year+1,+1):
        #draw the chart line by line: year+"|"+sea level/5*" "+"*"
        print(str(n)+"|"+(int(round(level/5)))*" "+"*");
        #data change
        level = level + rate;
        rate = rate + accel;
    #print the x coordinate of the graph
    print(" "+"+"+(int(round(level/5)))*"-");

if __name__ == '__main__':
	main();
    


        
        