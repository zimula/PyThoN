#Here I will test object methods. 
    #they are included in the class. 
class Cats:
	def __init__ (self, name, specie, gender):
		self.name = name
		self.specie = specie
		self.gender = gender
	def __str__(self) :
		return f"Name: {self.name}, Specie: {self.specie}, Gener: {self.gender}"
	def animalSound(self):
		print("The cat says meow!")
		
    #testing it
cat1 = Cats("Tom", "Tiger", "Male")
print(cat1)
cat1.animalSound()