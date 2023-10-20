import numpy as np

class Stock:
    num_stocks = 0
    analyst = " the Bureau"
    'use inheritance to override'

    
    def __init__(self, symbol):
        self.symbol = symbol
        self.price_history = []
        'list made up of tuples'
        Stock.num_stocks = Stock.num_stocks +1
        'instance tracking'
        
    
    def stock_tracking(self):
        return Stock.num_stocks

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        self.price_history.append((timestamp,price))
        'add () around parameters if pairs etc'

    def get_price_history(self):
        return self.price_history[-1][1] 
    

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
    

    'trend using mean of relative change'
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
        
    'risk using std'
    def risk_level(self):
        prices = [price for _,price in self.price_history]
        'calculate daily returns'
        '(today-yesterday)/yesterday = a day"s return.'
        returns = np.diff(prices)/ prices[:-1]
        'std as risk'
        risk = np.std(returns)

        low_risk = 0.05
        high_risk = 0.15

        if risk < low_risk:
            return ':-) low volatility past'
        elif risk < high_risk:
            return ':-| moderate volatility past'
        else:
            return ':-( very volatile past'

class Analyst(Stock):
    def __init__(self, analyst):
        super().__init__(analyst)
        self.analyst = analyst
    



