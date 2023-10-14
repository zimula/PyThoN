import pandas as pd

excel_file_path = r"C:\\Users\\zimul\\Documents\\python\\classes+unitTests\\stockAnalysis\\Book1.xlsx"
df = pd.read_excel(excel_file_path)
print(df.head())