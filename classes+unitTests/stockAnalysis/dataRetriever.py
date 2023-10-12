import pandas as pd
from stock import Stock

class DataRetriever:
    def __init__(self, excel_file) -> None:
        self.excel_file = excel_file
    
    'retrieving method'
    def retrieve_data(self):
        try:
            data = pd.read_excel(self.excel_file)
            return data
        except Exception as e:
            return f"Data retrieval failed: {str(e)}"
        
    'instantiate stock from data retrieved'
    def instantiate_stock_from_data(self):
        data = self.retrieve_data()
        stocks = {}
        if isinstance(data, pd.DataFrame):
            for index, row in data.iterrows():
                symbol = row['Symbol']
                date = row['Date']
                price = row['Price']

                if symbol not in stocks:
                    stock = Stock(symbol)
                    stocks[symbol] = stocks
                else:
                    stock = stocks[symbol]

                stock.update(data, price)
            return list(stocks.values())
        else: 
            return None