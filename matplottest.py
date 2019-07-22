# %matplotlib inline     --> jupyter
import numpy as np
import matplotlib.pyplot as plt
import random

x = np.array([1, 2, 3, 4])
y = np.array([5, 7, 6, 3])

plt.plot(x,y)
plt.xlabel("X-Achse")
plt.ylabel("Y-Achse")
plt.show()

plt.scatter(x, y)		#points not connected
plt.show()
#plt.savefig('foo.png')

x = [i for i in range(1, 51)]
y = [random.randint(0, 50) for i in range(50)]

plt.scatter(x, y)
plt.show()