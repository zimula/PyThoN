from concrete_commands import *
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