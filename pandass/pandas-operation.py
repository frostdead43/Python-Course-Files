import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x*x

kareal2 = lambda x: x*x

result = df
result = df["Column2"].unique() #eşsiz olanları seçme
result = df["Column2"].nunique() #eşsiz sayısı
result = df["Column2"].value_counts() # kaç kez tekrarlandı
result = df ["Column1"].apply(kareal) # result = df["Column1"] * 2
result = df ["Column1"].apply(lambda x: x*x)
result = df ["Column3"].apply(len)
df["Column4"] = df["Column3"].apply(len)
result = df.columns
result = df.index
result = df.info
result = df.sort_values("Column2") #sıralama

#pivot table önemlii

# print(df)
print(result)