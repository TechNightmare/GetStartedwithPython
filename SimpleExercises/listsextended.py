import matplotlib.pyplot as plt
import numpy as np
#list comprehension
list = [3*i for i in range(1, 10, 3)]

print(list)

x = [[1, 2, 3, 4], 
	[5, 7, 9, 12]]

plt.scatter(x[0][:], x[1][:])
#plt.show()

a = np.array([[1,2],[3,4]], dtype = np.float16)
print(a)

print(a.T)	#transponierte Matrix
print(np.transpose(a))

a = a.astype(np.float32)
print(a.dtype)

print(a.shape)

b = np.zeros(shape = (3,2))
print(b)
print(b.T)