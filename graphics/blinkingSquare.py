from graphics import *
import random

# A SQUARE THAT CONTINUOUSLY CHANGES COLORS

win = GraphWin("BLINKING SQUARE", 300, 300)

x1, y1 = 50, 50
x2,y2 = 150, 150

square = Rectangle(Point(x1,y1),Point(x2,y2))

try:
    while True:
        #randomize color
        random_color = color_rgb(random.randint(0,255), random.randint(0,255),random.randint(0,255))
        square.setOutline(random_color)
        square.setFill(random_color)
        
        
        square.draw(win)
        time.sleep(1)

        square.undraw()
except GraphicsError:
    win.close()