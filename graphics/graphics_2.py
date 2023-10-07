'making shapes'
from graphics import *

'create canvase: graphwin(title, size)'
win = GraphWin("Shapes", 500,500)

'create circle'
center = Point(100,100)
'circle(center, radius)'
circ = Circle(center, 30)
circ.setFill('red')
circ.draw(win)

'add text to circle'
label = Text(center, "Red circle")
label.draw(win)

'create square'
rect = Rectangle(Point(30,30),Point(70,70))
rect.setFill("blue")
rect.draw(win)

'create a line'
line = Line(Point(20,30),Point(180,165))
line.draw(win)

'create an oval'
oval = Oval(Point(20,150),Point(180,199))
oval.setFill("yellow")
oval.draw(win)

win.getMouse()
win.close()