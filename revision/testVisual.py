from graphics import *


'list to draw'
items = ["item1", "Item2", "item3"]

'methods to manipulate list'
def add_items():
    if len(items)< 12:
        x= str(len(items)+1)
        items.append('item'+ x)
    

def remove_items():
    """ for item in items:
        if item == i:
            items.remove(item) """
    'for now LIFO will do'
    items.pop(0)

'button methods'
def button1_click():
    add_items()
    redraw_blocks()
def button2_click():
    remove_items()
    redraw_blocks()
def end_it():
    win.close()

def redraw_blocks():
    for i in win.items[:]:
        if isinstance(i, Rectangle) and i is not button1 and i is not button2 and i is not button3:
            i.undraw()
    for i in win.items[:]:
        if isinstance(i, Text) and i is not label1 and i is not btn1_lable and i is not btn2_lable and i is not btn3_lable:
            i.undraw()
    
    'initial y-coordinate for first block'
    y = win.getHeight() - 200
        
    'draw blocks'
    for item in items:
        'position on x axis'
        x = win.getWidth()//2
        '2 points around x and y + block_height'
        'half the block on the left of x and the other on the right'
        block = Rectangle(Point (x - block_width // 2, y), Point(x + block_width // 2, y + block_height))
        block.setFill('grey')
        block.draw(win)
        label = Text(Point(x, y + block_height // 2), item)
        label.draw(win)
        y -= block_height + 5

win = GraphWin("Warehous", 600, 600)

'item dimensions'
block_width = 80
block_height = 30
    
'initial y-coordinate for first block'
y = win.getHeight() - 200
    
'draw blocks'
for item in items:
    'position on x axis'
    x = win.getWidth()//2
    '2 points around x and y + block_height'
    'half the block on the left of x and the other on the right'
    block = Rectangle(Point (x - block_width // 2, y), Point(x + block_width // 2, y + block_height))
    block.setFill('grey')
    block.draw(win)
    label = Text(Point(x, y + block_height // 2), item)
    label.draw(win)
    y -= block_height + 5

'static elements'
label1 = Text(Point(win.getWidth()//2, win.getHeight() - 80),'FIFO Warehouse: max. 12')
label1.setSize(14)
label1.setStyle('bold')
label1.draw(win)
'2 buttons to call add and delete methods.'
button1 = Rectangle(Point(450, 100),Point(500, 130))
btn1_lable = Text(Point(475, 115), 'add')
button1.setFill('green')

button2 = Rectangle(Point(450, 150),Point(500, 180))
btn2_lable = Text(Point(475, 165), 'remove')

button3 = Rectangle(Point(450, 50),Point(500, 80))
btn3_lable = Text(Point(475, 65), 'X')

button1.setFill('green')
button1.draw(win)
btn1_lable.draw(win)
button2.setFill('orange')
button2.draw(win)
btn2_lable.draw(win)
button3.setFill('red')
button3.draw(win)
btn3_lable.draw(win)

'my event listener'
while True:
    click_point = win.getMouse()
    if 450 <= click_point.getX() <= 500 and 100 <= click_point.getY() <= 130:
        button1_click()
    elif 450 <= click_point.getX() <= 500 and 150 <= click_point.getY() <= 180:
        button2_click()
    elif 450 <= click_point.getX() <= 500 and 50 <= click_point.getY() <= 80:
        end_it()
    
