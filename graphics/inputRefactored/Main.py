from graphics import *
import time
from DataManager import DataManager
from Person import Person
from CreateForm import Form

def main():
    win, name_entry, age_entry, update_button, details_text, table, table_color = Form.create_form()
    Person.persons = DataManager.getData('Persons.txt')
    Form.updateTable(Person.persons, table)
    
    try:
        while True:
            key = win.getKey()
            if key == 'Return':
                name = name_entry.getText()
                age = age_entry.getText()
                if name and age:
                    new_person = Person(name,age)
                    details_text.setText(f'Created person: Name: {new_person.name}, Age: {new_person.age}, ID: {new_person.getID()}')
                    Form.updateTable(Person.persons, table)
                time.sleep(2)
                name_entry.setText('')
                age_entry.setText('')
                details_text.setText('')
                DataManager.saveData(Person.persons, 'Persons.txt')
            elif key == 'd':
                #field to hold id to delete.
                Person.deleteByID('field value')
    
    except KeyError:
        print('keys')
    except GraphicsError:
        win.close()

if __name__ =='__main__':
    main()

    