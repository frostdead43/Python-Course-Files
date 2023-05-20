import matplotlib.pyplot as plt
import numpy as np

# x = [1,2,3,4]
# y = [1,4,9,16]

# plt.plot(x,y,"o--r") 
# plt.axis([0,6,0,20])

# plt.title("Grafik basligi")
# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.show()

""""""
# x = np.linspace(0,2,100)

# plt.plot(x, x, label="linear",color="red")
# plt.plot(x, x**2, label ="quadratic",color="blue")
# plt.plot(x, x**3, label ="cubic",color="orange")

# plt.xlabel("x label")
# plt.ylabel("y label")

# plt.title("benim grafik")

# plt.legend()
# plt.show()

""""""
# x = np.linspace(0,2,100)
# fig,axs = plt.subplots(3)

# axs[0].plot(x, x,color="red")
# axs[0].set_title("linear")

# axs[1].plot(x, x**2,color="blue")
# axs[1].set_title("quadratic")

# axs[2].plot(x, x**3,color="orange")
# axs[2].set_title("cubic")

# plt.tight_layout()
# plt.show()

""""""
# x = np.linspace(0,2,100)
# fig,axs = plt.subplots(2,2)
# fig.suptitle("grafik basligi")

# axs[0,0].plot(x, x,color="red")
# axs[0,1].plot(x, x**2,color="blue")
# axs[1,0].plot(x, x**3,color="orange")
# axs[1,1].plot(x, x**4,color="green")
# plt.show()

""""""

import pandas as pd
df=pd.read_csv("nba.csv")

df= df.drop(["draft_number"],axis= 1).groupby("team").mean()
df.plot(subplots=True)
plt.tight_layout()
plt.legend()
plt.show()