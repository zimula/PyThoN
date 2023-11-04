import DataManager
import Person
import CreateForm

def main():
    win, name_entry, age_entry, update_button, details_text, table, table_color = CreateForm.Form.create_form()
    Person.Person.persons = DataManager.DataManager.getData('Persons.txt')

    