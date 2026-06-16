import pandas as pd

df=pd.read_csv("Excel.1.csv")
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull())
print(df.shape)