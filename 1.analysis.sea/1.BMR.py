#Aisha Ramos, Yining Hua
#BMR.py
#Lab1
#Computes the Basal Metabolic Rate (for women)

#a function to calculate calories based on given data
def calcBMR(weight,ft,inch,age):
    height = ft*12+inch;
    BMR = 655 + 4.35 * (weight) + 4.7 * (height) - 4.7 * (age);
    return(round(BMR,1)); 

def main():
    print ("This program illustrates a chaotic function.");
    #get the parameters
    ft,inch = eval(input("height:_____feet, ____inches:"));
    weight = eval(input("weight in lbs: "));
    age = eval(input("What's your age?: "));
    #run the calcBMR function under main()
    print("The colories you burn per day if you stayed motionless is",calcBMR(weight,ft,inch,age),"cal/day");
        
if __name__== '__main__':
    main();
        
        

    


    
