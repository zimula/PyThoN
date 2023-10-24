from graphics import *
from Invoker import Calculator
from concrete_commands import *
from fractions import Fraction
'Main (should probably put everything in its own module) '
def main():
    'gui'
    win = GraphWin("float calculator", 600, 600)
    win.setBackground('orange')
    x = win.getWidth()
    y = win.getHeight()
    intro = Text(Point(x-300, y -100 ), "powered by Command-Pattern")
    intro.setFace("helvetica")
    intro.setStyle("bold italic")
    intro.setTextColor('orangered')
    intro.setSize(30)
    intro.draw(win)
    
    'input'
    text1 = Text(Point(100,50), "First no.")
    entry1 = Entry(Point(250, 50), 20)
    text2 = Text(Point(100,100), "Second no.")
    entry2 = Entry(Point(250, 100), 20)
    

    text1.draw(win)
    text2.draw(win)
    'order of drawing sets focus on the last drawn'
    entry2.draw(win)
    entry1.draw(win)

    'choosing operation'
    opText = Text(Point(120, 150), "Select Operation")
    opText.setStyle('bold')
    opText.draw(win)

    'buttons: loaded into list based on items in operations list'
    opButtons = []
    opSympbols = ['+','-','*','/']
    for i, opSympbol in enumerate(opSympbols):
        button = Rectangle(Point(60,180 + i*35),Point(200, 210+i*35))
        buttonText = Text(button.getCenter(),opSympbol)
        buttonText.setSize(20)
        buttonText.setTextColor('green')
        button.setFill('blue')
        button.draw(win)
        buttonText.draw(win)
        'load button to opButtons'
        opButtons.append((button, buttonText))

    'output'
    resultText = Text(Point(400,200),"ghgh")
    resultText.setSize(25)
    resultText.setStyle('bold')
    resultText.draw(win)


    'using invoker'
    calculator = Calculator()
    while True:
        try:
            'invent listener'
            click_point = win.getMouse()
            for button, buttonText in opButtons:
                left, top = button.getP1().getX(), button.getP1().getY()
                right, bottom = button.getP2().getX(), button.getP2().getY()
                if left < click_point.getX() < right and top < click_point.getY() < bottom:
                    selectedOp = buttonText.getText()
                    opText.setText(f'{selectedOp}')
            
            'getting the values'
            x = Fraction(entry1.getText())
            y = Fraction(entry2.getText())
        
            
            operation = selectedOp

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
            result = calculator.calculate(x,y)
            resultText.setText(result)
            print(f'Result: {result}')
        except GraphicsError:
            break
    win.close()
        
if __name__ == '__main__':
    main()
