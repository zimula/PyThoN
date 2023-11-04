#class to create form. Static methods, no instantiation required.
from graphics import * 
class Form():
    @staticmethod
    def create_form():
        win = GraphWin("Person registry", 600, 600)
        #set range of coordiate system.
        win.setCoords(0,0,10,10)
        win.setBackground("orangered")
        #labels and entry field
        age_label = Text(Point(1,7.5), "Age:")
        age_label.setSize(12)
        age_label.setStyle("bold")
        age_label.draw(win)
        age_entry = Entry(Point(2.4,7.5), 12)
        age_entry.draw(win)
        
        name_label = Text(Point(1,8), "Name:")
        name_label.setSize(12)
        name_label.setStyle("bold")
        name_label.draw(win)
        name_entry = Entry(Point(2.4,8), 12)
        name_entry.draw(win)

        update_button = Rectangle(Point(1.7,5),Point(3, 6))
        update_button_label = Text(update_button.getCenter(), "Enter to Update")
        update_button.setWidth(40)
        update_button_label.setTextColor("white")
        update_button_label.setStyle('bold')

        update_button.draw(win)
        update_button_label.draw(win)

        warning_lable = Text(Point(6, 9.7), "Creates txt in folder to save persons")
        warning_lable.draw(win)

        details_text = Text(Point(6,9), "result")
        details_text.setSize(12)
        details_text.setStyle("bold")
        details_text.setTextColor("white")
        details_text.draw(win)

        table_color = Rectangle(Point(4,0),Point(10,8.7))
        table_color.setFill("red")
        table_color.draw(win)

        table = Text(Point(6,5), "")
        table.setSize(12)
        table.setTextColor("white")
        table.setStyle("bold")
        table.draw(win)
        
        return win, name_entry, age_entry, update_button, details_text, table, table_color