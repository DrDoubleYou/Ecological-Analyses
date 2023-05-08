import csv
import pandas as pd

with open("trees.csv", "r") as t:
    reader  = list(csv.reader(t))

trees=[[],[],[],[]]
all_trees = set()

for row in reader[1:]:
    for area in range(len(row)):
        if area !="":
          trees[area].append(row[area])
          all_trees.add(row[area])
          
data = {"Species":sorted(list(all_trees)),"OG":"","MT":"","LT":"","CC":""}

df = pd.DataFrame(data)

print(len(df.columns))

for i in range(len(df)):
    for column in range(1,len(df.columns)):
        if df.iloc[i,0] in trees[column-1]:
            df.loc[i,df.columns[column]] = "x"

df.to_csv("trees_final.csv",index=False)