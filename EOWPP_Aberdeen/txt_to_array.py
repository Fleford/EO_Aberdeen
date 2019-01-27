import numpy as np
import matplotlib.pyplot as plt


def txt_to_array(filepath):
    with open(filepath, "r") as read_f:
        with open("col_fixed_" + filepath, "w") as write_f:
            ncol = 0
            for i, line in enumerate(read_f):
                line_array = line.split()
                if i == 0:
                    ncol = len(line_array)
                for val in line_array:
                    write_f.write("\t" + val)
                if len(line_array) != ncol:
                    write_f.write("\n")
    return np.loadtxt("col_fixed_" + filepath)


array = txt_to_array("abr2_kx.txt")
print(array.dtype)
# plt.imshow(array, cmap="Purples", extent=[300, 100, 300, 100])
plt.imshow(array, cmap="jet", alpha=0.8)
plt.colorbar()
plt.plot(200, 116, "gx")
plt.annotate(1.0, (200, 116))
plt.plot(298, 100, "g.")
plt.plot(178, 117, "r.")
# plt.xlim(100, 300)
# plt.ylim(300, 100)
plt.savefig('Layer2_kx.pdf')
plt.show()
