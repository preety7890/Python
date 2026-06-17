import pandas as pd

data={
    "Name":["Rahul"," Aman","Priya",None],
    "Marks":[78,None,92,85],
    "City":["Delhi","DELHI","delhi","Delhi"]

}

df=pd.DataFrame(data)
print(df)

# 1 checking missing values
print(df.isnull().sum())

# 2 fill missing values

print(df['Marks'].fillna(df["Marks"].mean()))

# 3 Removes spaces
print(df['Name'].str.strip())

# 4 standardize city name

print(df["City"].str.capitalize())

# 5 Generate average marks
print(df["Marks"].mean())

