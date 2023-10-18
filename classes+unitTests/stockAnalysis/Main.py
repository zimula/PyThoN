'using the the stock and dataRetriever modules'
from dataRetriever import DataRetriever




'Instantiate data object'
data_retriever = DataRetriever(r"stockAnalysis\\Book2.xlsx")


'instantiate stock using data'
stocks = data_retriever.instantiate_stock_from_data()

'if succeful, apply object methods'
if stocks:
    print("Not Financial Advice")
    print("**************")
    for stock in stocks:
        print(f"Symbol: {stock.symbol}")
        print("Price:", stock.get_price_history(), "dkk")
        print('24Hr:', stock.daily_price_change(), "%")
        print(stock.price_increase_trend())
        print("Volatility: N/A")
        print("=====================================================")
else:
    print("error")




'to make sure that main run when this modules is executed as main method'