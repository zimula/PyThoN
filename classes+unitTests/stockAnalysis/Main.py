'using the the stock and dataRetriever modules'
from dataRetriever import DataRetriever



'enter file to open'
data_retriever = DataRetriever(r"C:\Users\zimul\Documents\python\classes+unitTests\stockAnalysis")

'instantiate using data'
stocks = data_retriever.instantiate_stock_from_data()

'if succeful, apply object methods'
if stocks:
    print("stock copied")
    for stock in stocks:
        print(f"Symbol: {stocks.symbol}")
else:
    print("error")

'to make sure that main run when this modules is executed as main method'