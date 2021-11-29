import math
def data():
    money = float(input("Amount of money you have: "))
    appleprice = float(input("Enter price of apples: "))
    return money, appleprice

def amount(cash,price):
    return cash // price
    
def applechange(cash, price):
    return cash % price

money,appleprice=data()

print(f"You can buy {amount(money,appleprice)} apple and your change is {applechange(money, appleprice):.2f} pesos.")
