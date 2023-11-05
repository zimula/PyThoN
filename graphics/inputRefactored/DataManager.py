import Person

class DataManager():

    @staticmethod
    def getData(filename):
        persons = [] 
        try:
            with open(filename, 'r') as file:
                for line in file:
                    variables = line.strip().split(',')
                    if len(variables) == 3:
                        id, name, age = variables
                        #if data format f'ed go to next line (try:except:)
                        try:
                            id = id.split(': ')[1]
                            name = name.split(': ')[1]
                            age = age.split(': ')[1]
                            persons.append(Person.Person(name, age))
                        except ValueError:
                            continue
        except FileNotFoundError:
            pass
        return persons

    @staticmethod
    def saveData(persons, filename): 
        with open(filename, 'w') as file:
            for person in persons:
                file.write(f'ID: {person.getID()}, Name: {person.name}, Age: {person.age}\n')
        file.close

""" 'Testing'

    #saving
person1 = Person.Person('Mark', 20)
person2 = Person.Person("Eddie", 25)
person3 = Person.Person('Ellie', 90)
person4 = Person.Person('Mary', 40)
test =[]
test.append(person1)
test.append(person2)
test.append(person3)
test.append(person4)
DataManager.saveData(test, 'Persons.txt')

    #loading
people = DataManager.getData('Persons.txt')
for i in people:
    print(i.getID(), i.name, i.age) """