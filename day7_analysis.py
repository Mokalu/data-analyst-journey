import pandas as pd

df =pd.read_csv("sales_clean.csv")
print(df.columns)

print(df["Global"].sum())
print(df.groupby("Genre") ["Global"].sum().sort_values(ascending=False))
#Top genre: Action with 136.85
print(df.groupby("Publisher") ["Global"].sum().sort_values(ascending=False))
#Top publisher: Activision with 72.44
print(df["Publisher"].value_counts().head())
print(df[["North America", "Europe", "Japan", "Rest of World"]].sum())
#Europe has the highest total per region with 211.57