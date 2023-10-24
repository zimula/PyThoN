from interfaces import ICommand
from fractions import Fraction

'my lcd finder'
def lcd(x, y):
    pass


'concrete commands to implement interface methods/ promises'
class command_add(ICommand):
    def execute(self, x, y):
        return x + y

class command_subtract(ICommand):
    def  execute(self, x, y):
        return x - y

class command_multiply(ICommand):
    def execute(self, x, y):
        return x * y

class command_divide(ICommand):
    def execute(self, x, y):
        return x / y