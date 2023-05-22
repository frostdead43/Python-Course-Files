import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index=["A","B","C"],columns=["Colomn1","Colomn2","Colomn3",])

result = df
result = df["Colomn1"]
result = df[["Colomn1","Colomn2"]]

result = df.loc ["A"]
result = df.loc[:,"Colomn1"]
result = df.loc[:,["Colomn1","Colomn2"]]
result = df.loc[:,"Colomn1":"Colomn3"]
result = df.loc["A":"C",:"Colomn2"]
result = df.loc["A","Colomn2"]

df["Colomn4"] = pd.Series(randn(3),["A","B","C"]) #kolon ekleme
df["Colomn5"] = df["Colomn1"] + df["Colomn3"]

print(df.drop("Colomn5",axis= 1)) # kolon silme

print(df)
print(result)