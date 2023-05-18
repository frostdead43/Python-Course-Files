ögrenciler = ["Emenuel Emenike","İsmail Cipe", "Anderson Talisca", "Mustafa Akbaş"]

def ögrenciEkle(names):
    ögrenciler.append(names)

def ögrenciSil(names):
    # ögrenciler.pop() sonöğrenci kaydını siler
    ögrenciler.remove(names)

def birdenfazlaögrenciekle(names):
    for i in names:
        ögrenciler.extend(names)

def listedeögrenciler(names):
    for i in names:
        print(ögrenciler)



def ögrencileriSil(names):
    i = 0
    while i < len(names):
        ögrenciler.remove(names[i])
        i+= 1



ögrenciEkle("Baki Mercimek")
ögrenciSil ("Anderson Talisca")
birdenfazlaögrenciekle(["Enner Goat Valencia","Felipe Melo"])
print(ögrenciler)
ögrencileriSil(["Emenuel Emenike","İsmail Cipe"])


