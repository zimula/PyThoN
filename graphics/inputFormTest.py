from graphics import *
import time
class Person():
    number_of_persons = 1
    pesons =[]
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = Person.number_of_persons
        Person.number_of_persons +=1
        Person.pesons.append(self)
        
    """ def assign_id(self):
        Person.number_of_persons +=1
        self.id = Person.number_of_persons
        Person.pesons.append((self.id, self.name, self.age)) """



""" person1 = Person('Emily', 30)
person2 = Person('Charlie', 20)
person3 = Person("Jane", 50) """

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

    #return win, entries and button
    return win, name_entry, age_entry, update_button, details_text, table, table_color

def update_table(table, persons):
    table_text = "Persons:\n"
    for person in persons:
        table_text  += f'ID: {person.id}, Name: {person.name}, Age: {person.age}\n'
    table.setText(table_text)

def save2record(filename, persons):
    with open(filename, 'w') as file:
        for person in persons:
            file.write(f'ID: {person.id}, Name: {person.name}, Age: {person.age}\n')

def load_instances(filename):
    persons = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    id, name, age = parts
                    try:
                        age = int(age.split(': ')[1])
                        name = str(name.split(': ')[1])
                        persons.append(Person(name, age))
                    except ValueError:
                        continue
    except FileNotFoundError:
        pass
    return persons    




def main():
    #references to hold return values from create_form()
    win, name_entry, age_entry, update_button, detail_text, table, table_color = create_form()
    #load instances from file and update table. 
    Person.pesons = load_instances('Persons.txt')
    update_table(table, Person.pesons)
    try:
       """  while True:
            click_point = win.getMouse()
            if update_button.getP1().getX() <= click_point.getX() <= update_button.getP2().getX() \
            and update_button.getP1().getY() <= click_point.getY() <= update_button.getP2().getY(): """
       #using key return key instead of click.
       while True:
            key = win.getKey()
            if key == 'Return':  
                name = name_entry.getText()
                age = age_entry.getText()
                if name and age:
                    new_person = Person(name, age)
                    detail_text.setText(f'Created person: Name: {new_person.name}, Age: {new_person.age}, ID: {new_person.id}')
                    update_table(table, Person.pesons)
                detail_text.setText("")
                age_entry.setText("")
                name_entry.setText("")
                save2record("Persons.txt", Person.pesons)

    except GraphicsError:
        win.close()


if __name__ == "__main__":
    main()









