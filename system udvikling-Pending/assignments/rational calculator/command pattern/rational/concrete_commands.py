from interfaces import ICommand


'my lcd finder'
def lcd(x, y):
    return x.denominator * y.denominator



'concrete commands to implement interface methods/ promises'
class command_add(ICommand):
    def execute(self, x, y):
        return (lcd /x.numerator)*x.numerator + (lcd / y.numerator)*y.numerator
        

class command_subtract(ICommand):
    def  execute(self, x, y):
        return (lcd/x.numerator)*x.numerator + (y.numerator)*y.numerator
        

class command_multiply(ICommand):
    def execute(self, x, y):
        return (x.numerator * y.numerator)/(x.denominator * y.denominator)

class command_divide(ICommand):
    def execute(self, x, y):
        return (x.numerator/x.denominator)*(y.denominator/ y.numerator)