#id changed to private. Requires a getter method. 
class Person():
    no_of_instances = 0
    persons = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.no_of_instances +=1
        self.__id = Person.no_of_instances
        Person.persons.append(self)
    def getID(self):
        return self.__id
    
    def deleteByID(self):
        Person.persons.remove(self)
    
    """ #the setter will look like this
    def fixID(self,newID):
        self.__id = newID """

""" person1 = Person('james', 40)
print(person1.getID())
for i in Person.persons:
    print(i.getID())
print(Person.no_of_instances) """
