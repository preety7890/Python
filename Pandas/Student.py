import pandas as pd
data = {
    "Name": ["Vivek", "Aman", "Rohit"],
    "Age": [21, 22, 23],
    "Marks":[70,58,87]
}
df=pd.DataFrame(data)
print(df.head())
print(df['Marks'].mean())
print("Total marks is:",df["Marks"].sum())
print("Highest marks is:",df["Marks"].max())
print("Lowest marks is:",df["Marks"].min())
