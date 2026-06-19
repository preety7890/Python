import pandas as pd

df=pd.read_csv("employees.csv")
print(df)
print(df.columns)

# clean the data
print(df.isnull().sum())

# find duplicates if present then remove it
print(df.duplicated())

# maximum salary
print(df[df["Salary"] == df["Salary"].max()])

print("==="*40)

# Employee earning above 50000
print((df["Salary"] > 50000).sum())
print((df[df["Salary"]>50000]['First Name']))

# Finances Employees
print(df[df['Team']=="Finance"])

print(df.columns)

# last login time in PM
print(df[df['Last Login Time'].str.endswith('PM')])

# last login time in AM
print(df[df['Last Login Time'].str.endswith('AM')])

# kon s team m kitne employee hai 
print(df.groupby('Team').size())

# all data in 2015
print(df[df['Start Date'].str.endswith('2015')])

print("==="*40)

print(df[df['Start Date'].str.endswith('2015') & df['Last Login Time'].str.endswith('PM')])

# year wise
print(df.groupby('Start Date').count())