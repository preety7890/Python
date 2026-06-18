import pandas as pd

df=pd.read_excel("marks_data.xlsx")
print(df)
print("=="*25)

# 1 topper
print(df[df["Marks"] == df["Marks"].max()])

# 2. Top 3 students
top3 = df.sort_values(by="Marks", ascending=False).head(3)
print(top3)

# 3. students above 80
print(df[df["Marks"]> 75])

# 4. python students
print(df[df["Course"]=="Python"])

# 5.students below 70
print(df[df["Marks"]<70])

# 6. students marks range between 60-75
print(df[(df["Marks"]> 60) & (df["Marks"]<75)])