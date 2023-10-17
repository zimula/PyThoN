class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []
        'list made up of tuples'

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        self.price_history.append((timestamp,price))
        'add () around parameters if pairs etc'


    'mimicing existing interface with property decorator'
    @property
    def price(self):
        return self.price_history[0:] if self.price_history else None
    
    'daily price change %'
    def daily_price_change(self):
        if len(self.price_history)<2:
            return "Not enough data for analysis"
        
        'daily change list'
        changes = []
        'tuple elements'
        yester_price = self.price_history[0][1] 
        
        'loop through list'
        for _, price in self.price_history[1:]:
            '_ is usde to ignore a variable'
            price_change = price - yester_price
            price_change_percent = (price_change/yester_price) * 100
            changes.append((_, price_change_percent))
            change_trend = changes
            yester_price = price
        return round(changes[-1][-1],2)
    

    'price trend: UNDER CONSTRUCTION'
    def price_increase_trend(self):
        trend = []
        old_price = self.price_history[0][1]
        for _, price in self.price_history[1:]:
            diff = price - old_price
            diff_percent = (diff/old_price)*100
            trend.append((_,diff_percent))
            avg = sum(i for _, i in trend )/ len(trend)
            old_price = price
        
        if avg > 0: 
            return self.symbol + " is in an Upward trend"
        elif avg < 0:
            return self.symbol + " is in a Downward trend"
        else:
            return self.symbol + " remains Constant"