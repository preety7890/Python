import pandas as pd
df=pd.read_excel("marks_data.xlsx")
print(df)

 # cleaning the data find null value
print(df.isnull())

# fill the missing value
df['Marks']=df['Marks'].fillna(df['Marks'].mean())
print(df['Marks'])


# correct course name and fill missing value with 'SQL'

df['Course'] = df['Course'].str.capitalize()
df['Course']=df['Course'].fillna('SQL')
print(df['Course'])

# remove spaces
df['Name']=df['Name'].str.strip()
print(df['Name'])

# remove duplicate value
df_duplicate=(df.duplicated())
print(df_duplicate)

drop_duplicate=(df.drop_duplicates(inplace=True))
print(drop_duplicate)

# fill missing value in age

print(df['Age'].dtype) # int and str both present then first convert it into numeric use =to_numeric

df['Age'] = pd.to_numeric(df['Age'], errors='coerce') 
# errors=coerce means "Agar koi value convert nahi ho sakti,
# to error mat do, us value ko NaN bana do."

df['Age']=df['Age'].fillna(df['Age'].mean())
print(df['Age'])

print(df)