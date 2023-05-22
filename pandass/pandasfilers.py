import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns= ["Column1","Column2","Column3","Column4","Column5"])

result = df
result = df.columns
result = df.head(7)
result = df.tail(7)
result = df["Column1"].head(3)
result = df.Column1.head(4) #üsttekinin alternatifi
result = df[["Column1","Column2"]].head()
result = df[5:15][["Column1","Column2"]]

result = df > 50
result = df[df>50]
result = df[df % 2==0]
result = df[df["Column1"] > 50] [["Column1","Column2"]]
result = df.query("Column1>= 50 & Column1 % 2 == 0")


print(result)