import pandas as pd

list = [["Ahmet",50],["Ali",60],["Yağmur",70], ["Çinar",80]]
dict = {"Name":["Ahmet","Ali","Yağmur","Çinar"], "Grade":[50,60,70,80]}
dict_list = [
                {"Name":"Ahmet","Grade":50},
                {"Name":"Ali","Grade":60},
                {"Name":"Yağmur","Grade":70},
                {"Name":"Çinar","Grade":80}
            ]


# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples=s1, oranges=s2)

# df= pd.DataFrame(data)
df = pd.DataFrame(dict_list,index= ["212","232","236","456"])
print(df)