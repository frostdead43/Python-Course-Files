import pandas as pd
df = pd.read_csv("nba.csv")
result = df

#1-ilk 10 kaydı getir
result = df.head(10)
#2-Toplam oyuncu sayısı
result = len(df.index)
#3- Yaşı 20-25 arasındaki oyunları isim ve oynadıkları takımlar
result = df[(df["age"] >= 20) & (df["age"]< 25)] [["playerName","team","age"]].sort_values("age", ascending= False)
#4- Anthony Mason isimli oyuncunun oynadıgı takim hagisi ?
result = df[(df["playerName"] == "Anthony Mason")]["team"]
#5- Kaç farklı takım mevcut ?
result = len(df.groupby("team"))
result = df["team"].nunique()
#6- Her takımda kaç oyuncu oynamaktadır ?
result = df["team"].value_counts()
#7- İsmi içinde "and" gecen kayıtları bulunuz.
result = df[df["playerName"].str.contains("and")]







print(result)