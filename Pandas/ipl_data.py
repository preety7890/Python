import pandas as pd

df=pd.read_csv("ipl_data.csv")
# print(df)

# starting 5 rows 
print(df.head())

# All null value if null value present
print(df.isnull().sum())


# all columns 
print(df.columns)

print(df['player_of_match'])

print(df.columns)

# All season which in 2016
print(df['season']==2016)

# All cities
print(df['city'])

# All city and season
print(df[['city','season']])

print(df[df['city']=='Delhi'].groupby('season').size())

print(df.groupby('season')['city'].size())

print(df['toss_winner'])

# who win maximum toss winner
print(df['toss_winner'].value_counts().idxmax())  # idxmax= return maximum value index

# who win minimum toss winner
print(df['toss_winner'].value_counts().idxmin())

#  how many time team win a toss

print(df.groupby('toss_winner').size())

print(df['winner'])

# which team win the most
print(df['winner'].value_counts().idxmax())

# How many time each team win 
print(df.groupby('winner').size())

print(df[['win_by_runs','winner']])
