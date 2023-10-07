import unittest
#figured out how to import class from another file 

class Test_TestIncDec(unittest.TestCase):
    #these 2 methods should fail because there is no reference to methods class. 
    def test_inc(self):
        self.assertEqual(inc_dec.inc(3),4)
    def test_dec(self):
        self.assertEqual(inc_dec.dec(3),4)

if __name__ == '__main__':
    unittest.main()