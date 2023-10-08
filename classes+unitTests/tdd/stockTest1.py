'improved and tests class Stock1'
import unittest
from HtmlTestRunner import HTMLTestRunner
import StockClass
from datetime import * 

class stockTest1(unittest.TestCase):
    
    def setUp(self):
        self.stock = StockClass.Stock1("TESLA")


    'price before update'
    def test_If_Price_Is_None(self):
        self.assertIsNone(self.stock.price)


    'check if price is none zero'
    def test_stockUpdate(self):
        self.stock.update(datetime(2014,2,12), price = 10)
        self.assertEqual(10, self.stock.price)


    'making sure the price is not negative'
    def test_NegativePrice(self):
        
        with self.assertRaises(ValueError):
            self.stock.update(datetime(2014,2,13),-1)


    'return latest price after update'
    def test_getLatestPrice(self):
        self.stock.update(datetime(2014,2,12),price=10)
        self.stock.update(datetime(2014,2,13),price=8.4)
        self.assertAlmostEqual(8.4, self.stock.price, delta=0.0001)
    

    'price Up-trend-true test'
    def test_increasingTrendTrue(self):
        timestamps = [datetime(2014,2,11),datetime(2014,2,12),datetime(2014,2,13)]
        prices = [8,10,12]
        for timestamp, price in zip(timestamps,prices):
            self.stock.update(timestamp, price)
        self.assertTrue(self.stock.price_increase_trend())

    'price uptrend false '
    def test_increasingTrendFalse(self):
        timestamps = [datetime(2014,2,11),datetime(2014,2,12),datetime(2014,2,13)]
        prices = [8,12,10]
        for timestamp, price in zip(timestamps,prices):
            self.stock.update(timestamp, price)
        self.assertFalse(self.stock.price_increase_trend())
    'some prices equal (flat)'
    def test_increasingTrendFlat(self):
        timestamps = [datetime(2014,2,11),datetime(2014,2,12),datetime(2014,2,13)]
        prices = [8,10,10]
        for timestamp, price in zip(timestamps,prices):
            self.stock.update(timestamp, price)
        self.assertFalse(self.stock.price_increase_trend())

        








'test if main and generate report.html'
if __name__=='__main__':
    custom_report_file_name = "TDD_StockTest1.html"
    runner = HTMLTestRunner(output='testsResults')
    unittest.main(testRunner=runner)