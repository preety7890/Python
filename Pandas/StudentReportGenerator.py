import pandas as pd

df = pd.read_csv("student_marks.csv")

print(df.head(10))
print(df.info())
print(df.shape)

print("="*10)

print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())


df.to_csv("student_report.csv", index=False)

