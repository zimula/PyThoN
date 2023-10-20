from vehicle import vehicle
class Human:
    def __init__(self, type, name, gender, age):
        self.type = type
        self.name = name
        self.gender = gender
        self.age = age
        self.vehicle = None
    def own_vehicle(self, vehicle):
        'will take instance of vehicle'
        self.vehicle = vehicle
        return f'{self.name} owns a {self.vehicle.model}'
    def going_out(self):
        if self.vehicle:
            self.vehicle.drive()
            return f'Driving to work in a {self.vehicle.model} from {self.vehicle.year}'
        else:
            return 'Taking train'
    def start_driving(self):
        if self.vehicle:
            return self.vehicle.drive()



""" mark = Human("","m","m", 50)
print(mark.going_out())
myCar = vehicle("toyota", "prius", 2002)
print(mark.own_vehicle(myCar))
print(mark.going_out())
print(mark.start_driving()) """
