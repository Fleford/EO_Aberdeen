import numpy as np

data = np.loadtxt("ib2_temp.dat", dtype=int)
print(data)
print(data.shape)

print()
test = np.array([[2,3,4], [5, 6, 7]])
print(test)
print(test.shape)
print(test[1, 2])
