'visual presentation of change in principal value'

def investment():
    C0 =  eval(input("Enter initial amount: "))
    n = 10
    interest = eval(input("Enter annual interest: "))
    for i in range(1,n+1):
        C0 = round(C0 * (1+interest),2)
        print('The value at the en of year ', i, " is ", C0)
investment()