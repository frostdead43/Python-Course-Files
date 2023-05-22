import pandas as pd

df = pd.read_csv("youtube.csv")
result = df
#1-ilk 10 kaydı getir.
result = df.head(10)
#2-İkinci 5 kaydı getir.
result = df[5:10].head(5)
#3-Dataset'de bulunan kolon isimleri ve sayısını bulunuz.
result = df.columns
result = len(df.columns)
#4-Aşagıda bulunan bazı kolonları silin ve kalan kolonları listeleyin.
#(thumbnail_link,comments_disabled,rating_disabled,video_error_or_removed)

# df = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis=1,inplace=True)
# result = df

#5-Like ve dislike sayılarının ortalamasını bulunuz.
result = df["likes"].mean()
result = df["dislikes"].mean()

#6-İlk 50 vid like ve dislike kolonlarını getirin.
result = df.head(50)[["title","likes","dislikes"]]
#7-En çok görüntülenen video hangisidir ?
result= df[df["views"].max() == df["views"]]
#8-En az görüntülenen  video hangisidir?
result= df[df["views"].min() == df["views"]]
#9-En fazla görüntülenen 10 video hangisidir?
result = df.sort_values("views",ascending=False).head(10) [["title","views"]]
#10- Kategoriye göre begeni ortalamalarını sıralı şekilde getiriniz
result = df.groupby("category_id").mean().sort_values("likes")["likes"]
#11- Kategoriye göre yorum sayılarınıı yukarıdan asagı sırala
result = df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]
#12-Her kategoride kaç video var?
result = df["category_id"].value_counts()
#13-Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz
df["title_len"] = df["title"].apply(len)
result = df
#14-Her video içinn kullanılan tag sayısını yen bir kolonda göster
df["tag_count"] = df["tags"]

#15-En popüler videoları listeleyiniz(like/dislike oranına göre)


def likedlikeoranhesapla(dataset):
    likelist=list(df["likes"])
    dislikelist=list(df["dislikes"])
    print(likelist,dislikelist)

    liste = list(zip(likelist,dislikelist)) #tuple listes (like,dislike sayıları)

    oranlistesi = []
    for like,dislike in liste:
        if(like+dislike) == 0:
            oranlistesi.append(0)
        else:
            oranlistesi.append(like/(like+dislike))
    return oranlistesi



    print(oranlistesi(df))




likedlikeoranhesapla(df)







# print(df)
# print(result)
