def add(x, y):
    return x + y
def sub(x,y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x/y


while True:
    x = float(input('"enter x value: '))
    y = float(input('"enter y value: '))
    operation = (input("enter operation: "))
    if operation == "+":
        result = add(x,y)
    elif operation == "-":
        result = sub(x,y)
    elif operation == "*":
        result = mult(x,y)
    elif operation == "/":
        result = div(x,y)
    print(result)
    break


        