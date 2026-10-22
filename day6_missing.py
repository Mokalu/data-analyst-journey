import pandas as pd

df = pd.read_csv("sales.csv",encoding="latin-1")
print(df.isnull().sum())
print(df.shape)
df["Publisher"].fillna("Unknown")
print(df.isnull().sum())
print(df.shape)
print(df.columns)

df["Publisher"]= df["Publisher"].str.strip()
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df.shape)