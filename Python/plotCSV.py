import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

path = "data.csv"

style.use('ggplot')

a = input("Appuyer sur entrer pour voir. ")
if a[-4:] == ".scv":
    path = a

x, y = np.loadtxt(path, unpack = True, delimiter = ",")

plt.title("Heartrate over time")
plt.ylabel("Heartrate")
plt.xlabel("Time (H:M:S)")
plt.show()