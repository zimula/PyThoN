import pandas as pd

excel_file_path = r"stockAnalysis\\Book1.xlsx"
df = pd.read_excel(excel_file_path)
print(df.head())

df = pd.read_csv("")