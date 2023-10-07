'''
A program to calculate change
 - this program has 2 data types
    integers: used as input
    floats: used to assign weights and in the result. 
    round(): can be used to turn floats into integers. 

    Plust a simple test of the math library. 
'''
import math
def change():
    print()
    print()
    print('Please enter the count of each coin type. ')
    quarters = eval(input('Quarters: '))
    dimes = eval(input('Dimes: '))
    nickels = eval(input('Nickels: '))
    pennies = eval(input('Pennies: '))
    total = round(quarters * .25 + dimes * .10 + nickels * 0.05 + pennies * .01,2)
    print()
    print('The total value of your change is', total)

change()
print(int(math.sqrt(4)))
