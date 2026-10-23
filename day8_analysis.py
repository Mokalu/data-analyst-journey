import pandas as pd
df= pd.read_csv("sales_clean.csv")

big = df[df["Global"] > 5]
print(big.shape)
#Games with Global sales over 5: 23
sim = df[df["Genre"] == "Simulation"]
print(sim.shape)
#simulation games: 23
japan_wins = df[df["Japan"] > df["North America"]]
print(japan_wins.shape)
#Japan beats North America: 138
df["NA_share"] = df["North America"] / df["Global"] * 100
print ("Average NA share:",df["NA_share"].mean())
#Average NA share: 38.829145546247396