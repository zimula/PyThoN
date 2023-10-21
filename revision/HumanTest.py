from Human import Human
from vehicle import vehicle
import unittest

class TestHumanMethods(unittest.TestCase):
    
    def setUp(self):
        self.car1 = vehicle("bmw", "m2", 2000)
        self.car2 = vehicle("mercedes", "s", 1999)
        self.human = Human("runner", "John", "m", "90")
    
    def test_ownVehicle(self):
        result = self.human.own_vehicle(self.car1)
        self.assertEqual(result, 'John owns a m2')
    
    def test_register(self):
         self.human.register_vehicle(self.car1)
         self.human.register_vehicle(self.car2)
         self.assertEqual(len(self.human.cars_owned), 2)
         
    def test_goingOutNoCar(self):
        result = self.human.going_out()
        self.assertEqual(result, 'Taking train')

    def test_goingOutWithCar(self):
        self.human.own_vehicle(self.car1)
        result = self.human.going_out()
        self.assertEqual(result, f'Driving to work in a {self.car1.model} from {self.car1.year}')
    
    def test_startDriving(self):
        self.human.own_vehicle(self.car2)
        result = self.human.start_driving()
        self.assertEqual(result, f'The {self.car2.model} has started moving.')

if __name__ == '__main__':
        unittest.main()