import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from GWM_Manipulator import extract_rivercells

# Wells
wells_DE = np.array([[16, 28],  # Row, Column (Total Fitness = 45059)
                     [15, 16],
                     [18, 14],
                     [8, 25]])
wells_PSO = np.array([[19, 28],  # Row, Column (Total Fitness = 53011)
                      [13, 14],
                      [17.1, 29.1],     # Offset added to points on the same cell
                      [16, 22]])
wells_EOWPP = np.array([[15, 19],   # Row, Column (Total Fitness = 53764)
                        [10, 23],
                        [19, 29],
                        [16.9, 28.9]])  # Offset added to points on the same cell
# Streamflow Constraint
strmflw_cnstrnt = np.array([[14, 14],
                         [14, 21],
                         [13, 23],
                         [15, 26]])
# Load in HK
SynthK = np.loadtxt("SynthHeteroK.txt")
print(SynthK, SynthK.shape)

# Setup empty grid model
data = np.ones((25, 30)) * np.nan  # Rows, Cols
# put river cells in matrix
rivercells = extract_rivercells()
for rivercell in rivercells:
    data[rivercell[0]-1, rivercell[1]-1] = 0
print("data")
print(data)
print(data.shape)

# make a figure + axes
fig, ax = plt.subplots(1, 1, tight_layout=True, figsize=(7.5, 5))
# make color map
river_cmap = matplotlib.colors.ListedColormap(['aqua'])
hk_cmap = matplotlib.colors.ListedColormap(['r', 'b'])
# set the 'bad' values (nan) to be white and transparent
river_cmap.set_bad(color='w', alpha=0)
# draw the grid
for row in range(data.shape[0]):
    ax.axhline(row, lw=1.1, color='k', zorder=5)
for col in range(data.shape[1]):
    ax.axvline(col, lw=1.1, color='k', zorder=5)

# plot the river cells and hk
hk_im = ax.imshow(SynthK, cmap=hk_cmap, extent=[0, SynthK.shape[1], 0, SynthK.shape[0]], alpha=0.3)
ax.imshow(data, interpolation='none', cmap=river_cmap, extent=[0, data.shape[1], 0, data.shape[0]], zorder=0)
# add colorbar for hk
cbar = plt.colorbar(hk_im)
cbar.ax.get_yaxis().set_ticks([])
for j, lab in enumerate(['$50$', '$500$']):
    cbar.ax.text(1.5, (j * 0.5) + 0.25, lab, ha='center', va='center', rotation=270)
cbar.ax.get_yaxis().labelpad = 30
cbar.ax.set_ylabel('Transmissivity [ft$^2$/day]', rotation=270)

# plot points
ax.plot([], [], color="aqua", marker="s", label="River cell", markersize=8, linestyle="None", markeredgecolor="k")
ax.plot(strmflw_cnstrnt[:, 1] - 0.5, data.shape[0] - strmflw_cnstrnt[:, 0] + 0.5, color="black", marker="*",
        label="Streamflow Depletion Constraint", markersize=8, linestyle="None")
ax.plot(wells_EOWPP[:, 1] - 0.5, data.shape[0] - wells_EOWPP[:, 0] + 0.5, "bo",
        label="EOWPP Well field (Total Fitness = 53764)")
ax.plot(wells_PSO[:, 1] - 0.5, data.shape[0] - wells_PSO[:, 0] + 0.5, "go",
        label="PSO Well field (Total Fitness = 53011)")
ax.plot(wells_DE[:, 1] - 0.5, data.shape[0] - wells_DE[:, 0] + 0.5, "ro",
        label="DE Well field (Total Fitness = 45059)")
# add legend
ax.legend(loc=2)
# Prepare x-axis ticks-n-labels
ax.set_xlabel("Model Columns")
ax.set_xticks(np.arange(data.shape[1]) + 0.5)
ax.set_xticklabels(np.arange(1, data.shape[1]+1), fontsize=7)
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
# Prepare y-axis ticks-n-labels
ax.set_ylabel("Model Rows")
ax.set_yticks(np.arange(data.shape[0]) + 0.5)
ax.set_yticklabels(np.arange(1, data.shape[0]+1)[::-1], fontsize=7)

plt.show()
# fig.savefig("Supply2_Benchmark_wellfields.pdf")
