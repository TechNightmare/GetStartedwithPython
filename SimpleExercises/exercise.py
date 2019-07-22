import matplotlib.pyplot as plt 
import random
import numpy as np

x = [i for i in range(0, 101)]
randdata = [random.randint(0, 70) for i in range(101)]


plt.scatter(x, randdata, color = "blue")
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")

#mean
mean = np.mean(randdata, dtype=np.float64)
plt.plot((0,101), (mean, mean), color = "red")

#median
median = np.median(randdata)
plt.plot((0, 101), (median,median), color = "yellow")

plt.show()