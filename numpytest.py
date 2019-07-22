#tests with numpy
import numpy as np
import matplotlib.pyplot as plt

array = np.array([1,2,3])

print(array.shape)	#dimension

array2 = np.array([1, 0, 2, 3])

array2 =  array2.reshape((2,2))

print(array2)

arrzero = np.zeros(shape = (4,2))

print(arrzero)

x = np.array([1, 2, 3, 4])
y = np.array([5, 7, 6, 3])

plt.plot(x,y)
plt.show

