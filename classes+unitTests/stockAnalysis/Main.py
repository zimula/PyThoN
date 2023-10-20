'using the the stock and dataRetriever modules'
from dataRetriever import DataRetriever
from stock import Analyst

def main():
    'Instantiate data object'
    data_retriever = DataRetriever(r"stockAnalysis\\Book2.xlsx")

    'instantiate stock using data'
    stocks = data_retriever.instantiate_stock_from_data()
    

    'if succeful, apply object methods'
    if stocks:
        user = Analyst(input('Please enter user name: '))
        print("Not Financial Advice")
        print("**************")
    
        for stock in stocks:
            print(f"Symbol: {stock.symbol}")
            print("Price:", stock.get_price_history(), "dkk")
            print('24Hr:', stock.daily_price_change(), "%")
            print(stock.price_increase_trend())
            print(stock.risk_level())
            print("=====================================================")
    
    else:
        print("error")

    print(f'Currently tracking {stock.stock_tracking()} stocks.')
    if user.analyst:
        print(f'Analysis performed by {user.analyst}')
    else: 
        print(f'Analysis performed by{stock.analyst}')
print("=====================================================")

if __name__ == "__main__":
    main()

'to make sure that main run when this modules is executed as main method'