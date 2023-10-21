class vehicle:
	cars_made = []
	cars_sold = []
	cars_inStock =[]
	cars = 1
	def __init__(self, brand, model, year):
		self.Id = vehicle.cars
		self.brand = brand
		self.model = model
		self.year = year
		self.driving = False
		self.made()
		vehicle.cars += 1
	
	def made(self):
		vehicle.cars_made.append((self.model, self.year))
		vehicle.cars_inStock.append((self.model, self.year))
	def sold(self):
		'run after human own a car'
		vehicle.cars_sold.append((self.model, self.year))
	def show_model(self):
		return self.model
	def show_brand(self):
		return self.brand
	def show_year(self):
		return self.year
	def update_year(self, year):
		year = input("Enter year")
		self.year = year
	def readable_view(self):
		return f'This car is a {self.model} and was made by {self.brand} in the {self.year}'
	def drive(self):
		if self.driving:
			return f'The {self.model} is already on the move.'
		else:
			self.driving = True
			return f'The {self.model} has started moving.'
	def park(self):
		if self.driving:
			self.driving = False
			return f'The {self.model} has been parked'
		else:
			return f'The {self.model} is already parking.'
		
print(vehicle.cars_sold)

""" 'Instantiation'
myCar = vehicle("toyota", "prius", 2002, False)
print(f'{myCar.brand} {myCar.model} {myCar.year}')

print(myCar.readable_view())
print(myCar.park())
print(myCar.drive())
print(myCar.drive())
print(myCar.park()) """

