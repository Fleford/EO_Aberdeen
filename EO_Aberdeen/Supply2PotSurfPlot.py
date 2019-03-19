import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from GWM_Manipulator import extract_rivercells


# Streamflow Constraint
strmflw_cnstrnt = np.array([[14, 14],
                            [14, 21],
                            [13, 23],
                            [15, 26]])
# Load in potentiometric surface
surf = np.loadtxt("Supply2_PotenSurf.txt")
surf = surf.reshape(25, 30)
print(surf, surf.shape)

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
fig, ax = plt.subplots(1, 1, tight_layout=True, figsize=(8, 5.5))
# make color map
river_cmap = matplotlib.colors.ListedColormap(['aqua'])
hk_cmap = matplotlib.colors.ListedColormap(['r', 'b'])
surf_cmap = plt.get_cmap('hsv', 20)
# set the 'bad' values (nan) to be white and transparent
river_cmap.set_bad(color='w', alpha=0)
# draw the grid
for row in range(data.shape[0]):
    ax.axhline(row, lw=0.5, color='k', zorder=5)
for col in range(data.shape[1]):
    ax.axvline(col, lw=0.5, color='k', zorder=5)

# plot the river cells and surf
# surf_im = ax.imshow(surf, extent=[0, surf.shape[1], 0, surf.shape[0]], cmap=surf_cmap)
# ax.imshow(data, interpolation='none', cmap=river_cmap, extent=[0, data.shape[1], 0, data.shape[0]], zorder=0)
print(np.arange(20,60,6))
print(np.arange(60,100,6))
print(np.concatenate((np.arange(20,60,6), np.arange(60,100,6))))
levels = np.concatenate((np.arange(20, 60, 4.5), np.arange(60,110,4.5)))
surf_fill = ax.contourf(np.flipud(surf),levels, cmap="hsv", extent=[0, data.shape[1], 0, data.shape[0]])
surf_lines = ax.contour(np.flipud(surf),levels, colors="k", extent=[0, data.shape[1], 0, data.shape[0]])
# ax.clabel(surf_lines, inline=1, fontsize=10)
cbar = plt.colorbar(surf_fill)
cbar.ax.get_yaxis().labelpad = 10
cbar.ax.set_ylabel('Hydraulic Head [feet]', rotation=270)


#Plot river cells
ax.plot(rivercells[:, 1] - 0.5, data.shape[0] - rivercells[:, 0] + 0.5, color="blue", marker="o",
        label="River cell", linestyle="None", markeredgecolor="white")
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
fig.savefig("Supply2_PotSurf.pdf")
