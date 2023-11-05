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
        
        age_label = Text(Point(0.5,7.5), "Age:")
        age_label.setSize(10)
        age_label.setStyle("bold")
        age_label.draw(win)
        age_entry = Entry(Point(2.4,7.5), 12)
        age_entry.draw(win)

        id2delete_lable = Text(Point(1.4,2.5), "Enter ID to delete")
        id2delete_lable2 = Text(Point(1.4,2), "Press Delete")
        id2delete_lable2.setSize(10)
        id2delete = Entry(Point(3,2.5),4)
        id2delete_lable.setSize(10)
        id2delete_lable.draw(win)
        id2delete_lable2.draw(win)

        id2delete.draw(win)
        
        name_label = Text(Point(0.5,8), "Name:")
        name_label.setSize(10)
        name_label.setStyle("bold")
        name_label.draw(win)
        name_entry = Entry(Point(2.4,8), 12)
        name_entry.draw(win)

        update_button = Rectangle(Point(1.7,5),Point(3, 6))
        update_button_label = Text(update_button.getCenter(), "Enter to Update")
        update_button.setWidth(40)
        update_button_label.setTextColor("white")
        update_button_label.setStyle('bold')
        update_button_label.setSize(10)
        update_button.draw(win)
        update_button_label.draw(win)

        warning_lable = Text(Point(6, 9.7), "Creates txt file in folder to save persons")
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
        table.setSize(8)
        table.setTextColor("white")
        table.setStyle("bold")
        table.draw(win)
        
        return win, name_entry, age_entry, id2delete, update_button, details_text, table, table_color
    
    def updateTable(persons, table):
        tableText = 'People \n'
        for person in persons:
            tableText += f'ID: {person.getID()}, Name: {person.name}, Age: {person.age}\n'
        table.setText(tableText)
