import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def txt_to_array(filepath):
    try:
        return np.loadtxt(filepath)
    except ValueError:
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


SynthK = txt_to_array("SynthHeteroK.txt")
print(SynthK, SynthK.shape)
# hkx = txt_to_array("abr2_kx.txt")
# mask = txt_to_array("ib2_ref.dat")
# print(mask.shape, hkx.shape)
# array = np.ma.masked_where(mask == 0, hkx)
# print(array)

my_cmap = matplotlib.colors.ListedColormap(['r', 'b'])
# # plt.imshow(array, cmap="Purples", extent=[300, 100, 300, 100])
plt.imshow(SynthK, cmap=my_cmap)
cbar = plt.colorbar()

cbar.ax.get_yaxis().set_ticks([])
for j, lab in enumerate(['$50$', '$500$']):
    cbar.ax.text(1.5, (j * 0.5) + 0.25, lab, ha='center', va='center', rotation=270)
cbar.ax.get_yaxis().labelpad = 30
cbar.ax.set_ylabel('Horizontal Hydraulic Conductivity [ft/day]', rotation=270)
for row in range((SynthK.shape[0])):
    plt.axhline(row + 0.5, lw=1, color='k', zorder=5)
plt.yticks([])
for x in range((SynthK.shape[1])):
    plt.axvline(x + 0.5, lw=1, color='k', zorder=5)
plt.xticks([])

plt.xlabel("Model Columns (1 cell = 200 ft)")
plt.ylabel("Model Rows (1 cell = 200 ft)")
# plt.plot(200, 116, "gx")
# plt.annotate(1.0, (200, 116))
# plt.plot(298, 100, "g.")
# plt.plot(178, 117, "r.")
# plt.xlim(100, 300)
# plt.ylim(300, 100)
# # plt.savefig('Layer2_kx.pdf')
plt.show()
