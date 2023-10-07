'testing input'
score1, score2 = eval(input("Enter 2 numbers separated by a comma: "))
average = (score1+score2)/2
print(int(average))

'''basic function
    - makes sure that code only fires when it's called like so;
    funcion()
'''
def convert():
    celsius = eval(input("Temp in Celsius: "))
    fahrenheit = (9/5) * celsius + 32
    print(fahrenheit)

convert()

'''definite loop
    - limited range loops.
    - no need calling a function multiple times with different arguments.  
'''
def loop(): 
    
    for i in range(1,eval(input("Enter number of iterations"))+1):
        x = i*i
        print(i," ", x)
loop()
