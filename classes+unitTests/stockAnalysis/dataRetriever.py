import pandas as pd
from stock import Stock
from datetime import datetime

class DataRetriever:
    def __init__(self, excel_file):
        self.excel_file = excel_file
    
    'retrieving method'
    def retrieve_data(self):
        try:
            'load data into data frame'
            data = pd.read_excel(self.excel_file)
            return data
        except Exception as e:
            return f"Data retrieval failed: {str(e)}"
        
    'instantiate stock from data retrieved'
    def instantiate_stock_from_data(self):
        data = self.retrieve_data()
        'dictioanary used to hold stock data'
        stocks = {}
        if isinstance(data, pd.DataFrame):
            'check if data is a 2d data structure'
            for index, row in data.iterrows():
                'set column headings'
                symbol = row['Symbol'] 
                date = row['Date']
                price = row['Price']

                if symbol not in stocks:
                    'if stock not in dictionary, instantiate'
                    stocks[symbol] = Stock(symbol)
                    
                'else use match'
                stock = stocks[symbol]

                stock.update(datetime.date(date), price)
            return list(stocks.values())
        else: 
            return None
        