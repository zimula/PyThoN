import datetime
class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        'adding price is none to make the test pass (is not tied to any parameter/ value)'
        self.price = None
    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price shoult not be negative")
            'to be retured on when number is < 0'
        self.price = price
    'price and date will be turned into a multidimensional array'