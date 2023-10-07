#An example of a simple class and object instantiation
class MyClass:
    x = 5
    greeting = "Hello"
    #creating an object from the class
obj1 = MyClass()
    #printing object values
print(obj1.x)
print(obj1.greeting)

# the __init__ Function: works as a constructor for the class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #creating object using __init__ constructor
person1 = Person("Martin", 45)
print(person1.name)
print(person1.age)
print(person1)

# the __str__funcion: what to return if object is represented as a string
class People():
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    #the __str__function
    def __str__(self):
        return f"{self.name} age {self.age}"
    #create object
people1 = People("James", 70)
print(people1)



