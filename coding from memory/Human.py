from vehicle import vehicle
class Human:
    def __init__(self, type, name, gender, age):
        self.type = type
        self.name = name
        self.gender = gender
        self.age = age
        self.vehicle = None
        self.cars_owned =[]
    def own_vehicle(self, car):
        'will take instance of vehicle'
        self.vehicle = car
        self.register_vehicle(self.vehicle)
        vehicle.sold(self.vehicle)
        return f'{self.name} owns a {self.vehicle.model}'
    def register_vehicle(self,vehicle):
        self.cars_owned.append(vehicle)
        return self.cars_owned
    def display_cars(self):
        for car in self.cars_owned:
            return car
    def going_out(self):
        if self.vehicle:
            self.vehicle.drive()
            return f'Driving to work in a {self.vehicle.model} from {self.vehicle.year}'
        else:
            return 'Taking train'
    def start_driving(self):
        if self.vehicle:
            return self.vehicle.drive()
    





'move this to main at some point'
mark = Human("","m","m", 50)
print(mark.going_out())
myCar = vehicle("toyota", "prius", 2002)
myCar2 = vehicle("toyota", "camri", 2010)
myCar3 = vehicle("toyota", "corola", 1995)
mark.own_vehicle(myCar)
mark.own_vehicle(myCar2)



print('============================================')
print('MANUFACTURING UPDATE')
for car in vehicle.cars_made:
    print(car[0], car[1])
print(f'{vehicle.cars-1} cars made so far.')
print('============================================')
print('SALES')
for i in vehicle.cars_sold:
    print(i[0], i[1])
print('=================================================')
print('MARK´S BEHAVIOUR')
print(f'{mark.name} owns the following cars:') 
for car in mark.cars_owned:
    print(f'{car.model} {car.year} from {car.brand}')
print(mark.going_out())



