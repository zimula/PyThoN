from interfaces import ICommand
from fractions import Fraction

'my lcd finder'
def lcd(x, y):
    return x.denominator * y.denominator

'concrete commands to implement interface methods/ promises'
class command_add(ICommand):
    def execute(self, x, y):
        return Fraction(x + y)
        

class command_subtract(ICommand):
    def  execute(self, x, y):
        return Fraction(x-y)
        

class command_multiply(ICommand):
    def execute(self, x, y):
        return Fraction((x.numerator * y.numerator)/(x.denominator * y.denominator))

class command_divide(ICommand):
    def execute(self, x, y):
        return Fraction((x.numerator/x.denominator)*(y.denominator / y.numerator))