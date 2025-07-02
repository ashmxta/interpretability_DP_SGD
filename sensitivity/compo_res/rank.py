import pandas as pd

infile = "sensitivity/compo_res/compo_res1.csv"
outfile = "sensitivity/compo_res/compo_res1_ranked.csv"

df = pd.read_csv(infile)
ranked = df.groupby("point")["Privacy cost"].sum().sort_values()
ranked.to_csv(outfile, header=["Total Privacy Cost"])

print("Saved ranked result to", outfile)
print("Lowest 10 privacy cost points:\n", ranked.head(10))
