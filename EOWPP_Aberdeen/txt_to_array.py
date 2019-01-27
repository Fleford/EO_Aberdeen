import numpy as np
import matplotlib.pyplot as plt

filepath = "abr2_kx.txt"

with open(filepath, "r") as read_f:
    with open("fixed_"+filepath, "w") as write_f:
        ncol = 0
        for i, line in enumerate(read_f):
            line_array = line.split()
            if i == 0:
                ncol = len(line_array)
            for val in line_array:
                write_f.write("\t"+val)
            if len(line_array) != ncol:
                write_f.write("\n")

array = np.loadtxt("fixed_"+filepath)
print(array.dtype)
plt.imshow(array, cmap="Purples")
plt.colorbar()
plt.plot(200, 100, "r.")
plt.plot(200, 200, "g.")
plt.plot(300, 300, "b.")
plt.savefig('Layer2_kx.pdf')
plt.show()
