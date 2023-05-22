import pandas as pd

personeller = {
    "Çalisan": ["Akif kyilmaz","Ahmet Can Erken","Kamil Zeng","Serhat Oğur","İbrahim Teymur","Batu Hatip","Linea Hamutenya"],
    "Meslek": ["Yazilimci","Psikolojik Danisman","Avukat","Boş","Asker","İşe alim","Öğretmen"],
    "Yaş": [30,25,45,50,23,34,42],
    "Semt": ["Kadiköy","Tuzla","Maltepe","Tuzla","Maltepe","Tuzla","Kadiköy"],
    "Maaş": [12000,9000,8000,400,7000,4000,10000]
}

df= pd.DataFrame(personeller)

result = df
result = df["Maaş"].sum()
result = df.groupby("Semt").groups

semtler = df.groupby("Semt")

# for name, group in semtler:
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Kadiköy")
result = df.groupby("Semt").sum()
result = df.groupby("Semt").mean()
result = df.groupby("Semt")["Çalisan"].count()



print(result)
