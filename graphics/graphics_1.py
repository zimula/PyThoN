'''
Objects: active data types that combine data and operations. 
    - interact by sending each other messages. 
Graphics: 
    - create canvas
    - create object
    - get coordinates
    - draw object
    '''
from graphics import *

'canvas where the graphics will appear'
win = GraphWin("Points and shapes")

'drawing a point (0.0 is located at the top left corner of the canvas)'
p = Point(10,10)
p.getX()
p.getY()
p.draw(win)

p2 = Point(140, 100)
p2.draw(win)

'add a line'
line = Line(p, p2)
line.draw(win)

'Keep canvas open until it is clicked.'
win.getMouse() 
win.close

