from graphics import *
'''
TAKING AN OOP APPROACH TO GRAPHICS. 
- All the shapes we draw are instances of a class in the module (point, circle, rectangle etc. )
- imagaine a smily face. This will require 2 circle object and an oval object.  

- each instance of the shape class also come with a bunch of methods. 
'''

win = GraphWin("SMILE", 500, 500)
'left eye'
leftEye = Circle(Point(80, 50), 5)
leftEye.setFill("yellow")
leftEye.setOutline("red")
leftEye.draw(win)

'right eye'
rightEye = Circle(Point(100,50),5)
rightEye.setFill('yellow')
rightEye.setOutline('red')
rightEye.draw(win)
'Instead of the above, we can just clone the left eye'

'mouth'
mouth = Oval(Point(75,60),Point(105,70))
mouth.setFill("red")
mouth.setOutline("black")
mouth.draw(win)

win.getMouse()
win.close()