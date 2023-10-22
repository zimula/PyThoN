'the interface'
class Command:
    def execute(self, x, y):
        pass

'concrete commands'
class command_add(Command):
    def execute(self, x, y):
        return x + y

'command invoker'
class Calculator:
    def __init__(self):
        self.command = None

    'command setter'
    def set_command(self, command):
        self.command = command
    
    'access command methods'
    def calculate(self, x, y):
        if self.command:
            return self.command.execute(x,y)
        else: 
            return 'no command set'

'Main'
calculator = Calculator()
calculator.set_command(command_add())

while True:
    x = float(input("Enter x value: "))
    y = float(input("Enter y value"))
    operation = input("Enter operation: ")
    if operation not in ['+', '-', '*', '/']:
        break
    elif operation == '+':
        result = calculator.calculate(x,y)
    print(result)
    break