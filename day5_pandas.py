import pandas as pd

df = pd.read_csv("sales.csv",
encoding="latin-1")
print(df.head())

#This command below shows (1034,9)
print(df.shape)

#This command below shows that the index are 'str'
print(df.columns)

#This command shows the publisher row, the string name: float 64 and dtype: object
print(df.dtypes)

print(df.describe())
#Comments
#Rows: 1034
#column: 9
#Text columns(object): 2
#Number columns: 6

print(df["Global"].sum())
print(df["Global"].mean())
print(df["Global"].max())
#Simulation appear most (23)
print(df["Genre"].value_counts())