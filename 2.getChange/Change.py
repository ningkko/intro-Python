#Yining Hua
#assignment2: Change.py
#simulates a vending machine that accepts a single bill, and then gives change according to the item's price.

def main():
    #call the function askPrice to get the money and the price    
    money_user,price = askPrice();

    listMoney = [1000,500,100,25,10,5,1];
    listMoneyname = ["$10 bill(s)","$5 bill(s)","$1 bills","quarter(s)","dime(s)","nickle(s)","pennie(s)"];
    changeCalc(listMoney,listMoneyname,money_user,price);
                  
                  
#function for asking value. easier to call again if the input's not the type we want
def askPrice():
    money_user = eval(input("Enter a single bill $(1,5,10 or 20):" ));
    price = eval(input("Enter the item price in two decimals $(e.g., 1.67):"));
    #evaluate the income: 1.money type right or not; 
    if (money_user != 20) and (money_user!=10) and (money_user!=5) and (money_user!= 1):
        print("No such bill");
        money_user,price=askPrice();
        #money enough or not;
    elif money_user<price:
        print("Your money is not enough.");
        money_user,price=askPrice();
    return money_user, price;

#function for calculating the change, can be reused for other currencies
def changeCalc(listMoney,listMoneyname,money_user,price):
    change = money_user - price;
    print("Change =",change);
    changeForCalc = change*100;
    for n in range (7):
        number = changeForCalc//listMoney[n];
        print(round(number),listMoneyname[n]);
        changeForCalc = changeForCalc%listMoney[n];
	
main();




