import matplotlib.pyplot as plt
import numpy as np

"""Örnek1"""

# x = [1,2,3,4]
# y = [1,4,9,16]

# plt.plot(x,y,"o--r") 
# plt.axis([0,6,0,20])

# plt.title("Grafik basligi")
# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.show()

"""Stack Plot"""
# yil = [2011,2012,2013,2014,2015]

# oyuncu1 = [8,10,12,7,9]
# oyuncu2 = [7,12,5,15,21]
# oyuncu3 = [18,20,22,25,19]

# plt.plot([],[],color="y",label="oyuncu1")
# plt.plot([],[],color="r",label="oyuncu2")
# plt.plot([],[],color="b",label="oyuncu3")

# plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])
# plt.title("yillara göre atilan goller")
# plt.xlabel("yil")
# plt.ylabel("gol sayisi")
# plt.legend()
# plt.show()

"""Pie Grafiği"""
# goal_types = "Penalti","Kaleye Atilan şut","Serbest Vurus"

# goals = [12,35,7]
# colors = ['y','r','b']

# plt.pie(goals,labels=goal_types,colors=colors, shadow=True,explode=(0.05,0.05,0.05), autopct = "%1.1f%%")
# plt.show()

"""Bar Grafigi"""
# plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="Bmw",width=.5)
# plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)

# plt.legend()
# plt.xlabel("Gün")
# plt.ylabel("Mesafe(km)")
# plt.title("Car informations")
# plt.show()



