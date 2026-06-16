import pandas as pd
data={
    "Name":["Rahul","Aman","Priya","Rohan"],
    "Marks":[78,85,92,65]
}

df=pd.DataFrame(data)

print("Total student is:",df['Name'].count())
print("Average marks is:",df['Marks'].mean())
print("Highest marks is:",df["Marks"].max())
print("Lowest marks is:",df["Marks"].min())