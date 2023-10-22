'the interface'
class Command:
    def execute(self, x, y):
        pass

'concrete commands'
class command_add(Command):
    def execute(self, x, y):
        return x + y

class command_subtract(Command):
    def  execute(self, x, y):
        return x - y

class command_multiply(Command):
    def execute(self, x, y):
        return x * y

class command_divide(Command):
    def execute(self, x, y):
        return x / y

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
        
'Main (should probably put everything in its own module) '
def main():
    calculator = Calculator()
    while True:
        x = float(input("Enter x value: "))
        y = float(input("Enter y value: "))
        operation = input("Enter operation: ")

        if operation not in ['+', '-', '*', '/']:
            break
        elif operation == '+':
            calculator.set_command(command_add())
        elif operation == '-':
            calculator.set_command(command_subtract())
        elif operation == '*':
            calculator.set_command(command_multiply())
        elif operation == '/':
            calculator.set_command(command_divide())
        result = round(calculator.calculate(x,y),2)
        print(result)
        break
if __name__ == '__main__':
    main()