from graphics import *
'visual presentation of change in principal value'

def investment():
    C0 =  eval(input("Enter initial amount: "))
    n = 10
    interest = eval(input("Enter annual interest: "))
    for i in range(1,n+1):
        C0 = round(C0 * (1+interest),2)
        print('The value at the en of year ', i, " is ", C0)

'the graph'
'win = GraphWin("Investemt growth", 320, 240)'
'''labels on the vertical axis
- centered at 20 pixels from the edge
- 50 pixels in height
- leaving 10 pixels at the bottom
'''
'Text(Point(20,230), "0.0K").draw(win)'
'Text(Point(20,180), "2.5K").draw(win)'
'Text(Point(20,130), "5K").draw(win)'
'Text(Point(20,80), "7.5K").draw(win)'
'Text(Point(20,30), "10K").draw(win)'

'''
HEIGHT:
- vertical range is 10k at 100px per interval
- this makes the ratio: 100/5000 = 0.2
- so, for co = 2000, the height is 230-(co*0.2) = 190.
- we will put this in a loop.
WIDTH:
- (320 - label_width)/number of bar)
    280 / 11 = 25

- THE RECTANGLE FORMULAR FOR THE FIRST RECTANGLE:
    rect(point(40,230),point(65, 230-C0*0.02))
    - bar width is calculate as year * 25+40:
    - the coordidates above are for year 0. 
'''

def investGraph():
    print("Investment growth")
    'C0 and intereste/year'
    C0 = float(input("Enter the initial investment: "))
    interest = float(input('Enter the desired interest/ year : '))

    'the labels'
    win = GraphWin("Investment growth", 320, 240)
    win.setBackground("grey")
    Text(Point(20,230), '0.0K').draw(win)
    Text(Point(20,180), '2.5K').draw(win)
    Text(Point(20,130), '5K').draw(win)
    Text(Point(20,80), '7.5K').draw(win)
    Text(Point(20,30), '10K').draw(win)

    'initial C0 bar'
    height = C0 * 0.02

    rect = Rectangle(Point(40,230), Point(65, 230-height))
    rect.setFill('yellow')
    'border width'
    rect.setWidth(2)
    rect.draw(win)

    'bar for remaining years'
    for i in range(1,11):
        barWidth = i * 25+40
        C0 = C0 * (1+interest)
        height = C0 * 0.02
        bar = Rectangle(Point(barWidth, 230),Point(barWidth+25, 230-height))
        bar.setFill('yellow')
        bar.setWidth(2)
        bar.draw(win)



    input("Press <Enter> to quit")
    win.close()
investGraph()
'''
MORE ON GRAPHICS:
- events
- get event data
- other ways of setting coordinates etc. 
'''