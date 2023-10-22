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
        print(add(x,y))
        break
    elif operation == "-":
        print(sub(x,y))
        break
    elif operation == "*":
        print(mult(x,y))
        break
    elif operation == "/":
        print(div(x,y))
        break

        