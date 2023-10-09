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
'************************************************************************'



'Improve stock class: price tracking implemented'
class Stock1:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        self.price_history.append((timestamp,price))
        'add () around parameters if multidimensional'


    'mimicing existing interface with property decorator'
    @property
    def price(self):
        return self.price_history[-1] if self.price_history else None
    
    'price trend'
    def price_increase_trend(self):
        'returns false if order does not fit'
        return self.price_history[-3]<\
        self.price_history[-2]<self.price_history[-1]
    
'Testing'
TSLA = Stock1("TSLA")
TSLA.update("2012-2-2",8)
TSLA.update("2012-2-3",10)
'data as strings'
as_String = "\n".join(f"{timestamp}: {price}" for timestamp, price in TSLA.price_history)

print(TSLA.price_history)
print(as_String)