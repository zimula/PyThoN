import unittest
from HtmlTestRunner import HTMLTestRunner
import StockClass
from datetime import * 

'expecting price to be none on instantiation'
class stockTest(unittest.TestCase):
    
    'instance to be used in each test. No need to repeat in each test'
    def setUp(self):
        self.stock = StockClass.Stock("TESLA")
    


    'price before update'
    def test_If_Price_Is_None(self):
        self.assertIsNone(self.stock.price)
        'this test should fail'
    
    
    
    'update method that holds a timestamp, price value, none-negative price, returns latest price'
    'only testing price value, date ignored for now'
    def test_stockUpdate(self):
        self.stock.update(datetime(2014,2,12), price = 10)
        self.assertEqual(10, self.stock.price)
    

    'making sure the price is not negative'
    def test_NegativePrice(self):
        try:
            self.stock.update(datetime(2014,2,13),-1)
        except ValueError:
            return
        self.fail("ValueError was not raised")    
        '''
        - can be rewritten using "self.assertRaises(ValueError, stock.update, datetime(),-1)
        '''

    'after multiple updates, it should return the latest price.'
    def test_getLatestPrice(self):
        self.stock.update(datetime(2014,2,12),price=10)
        self.stock.update(datetime(2014,2,13),price=8.4)
        self.assertAlmostEqual(8.4, self.stock.price, delta=0.0001)
        'compare latest to the current price to the 4th decimal and date is ignore.'








'test if main and generate report.html'
if __name__=='__main__':
    custom_report_file_name = "TDD_StockTest.html"
    runner = HTMLTestRunner(output='tests')
    unittest.main(testRunner=runner)
