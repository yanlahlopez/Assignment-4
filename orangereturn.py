import math

def quantity():
    apple = int(input("How many apples do you want? "))
    orange = int(input("How many oranges do you want? "))
    return apple, orange

def product():
   appletotal = apple * 20
   orangetotal = orange * 25 
   return appletotal, orangetotal

def total(aamount,oamount):
    return aamount + oamount

apple, orange=quantity()
appletotal, orangetotal=product()

print(f"The total amount is {total(appletotal,orangetotal)}.")
