from graphics import *
import random
import time

win = GraphWin("moving square", 600, 600)

x1, y1 = 50, 50
x2, y2 = 150, 150

x3, y3 = 200, 200
x4, y4 = 400, 400

square = Rectangle(Point(x1, y1), Point(x2, y2))
square1 = Rectangle(Point(x3, y3), Point(x4, y4))



square.draw(win)
square1.draw(win)

dx, dy = random.triangular(1,5,2.5),random.triangular(1,5,2.5)
dx1, dy1 = random.gauss(0,1), random.gauss(0,1)

try:
    while True:
        random_color = color_rgb(random.randint(0,255), random.randint(0,255),random.randint(0,255))
        square.move(dx, dy)
        square.setFill(random_color)
        square1.move(dx1, dy1)
        
        #gauss distribution
        red = int(random.gauss(128,50))
        green = int(random.gauss(128,50))
        blue = int(random.gauss(128,50))
        #limit with rgb range 
        red = max(0, min(255,red))
        green = max(0, min(255,green))
        blue = max(0, min(255,blue))
        random_color1 = color_rgb(red, green, blue)

        square1.setFill(random_color1)

        p1 = square.getP1()
        p2 = square.getP2()

        if square.p1.getX() <= 0 or square.p2.getX() >= win.getWidth():
            dx = -dx
        if square.p1.getY() <= 0 or square.p2.getY() >= win.getHeight():
            dy = -dy

        if square1.p1.getX() <= 0 or square1.p2.getX() >= win.getWidth():
            dx1 = -dx1
        if square1.p1.getY() <= 0 or square1.p2.getY() >= win.getHeight():
            dy1 = -dy1

        if win.checkMouse():
            break

        time.sleep(0.084)
        
        
        

except GraphicsError:
    win.close()

