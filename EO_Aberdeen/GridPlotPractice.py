import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from GWM_Manipulator import extract_rivercells


test_parameters = np.array([[12, 11],  # Row, Column
                            [16, 17],
                            [14, 25]])
data = np.ones((25, 30)) * np.nan  # Rows, Cols
# put river cells in matrix
rivercells = extract_rivercells()
for rivercell in rivercells:
    data[rivercell[0]-1, rivercell[1]-1] = 0
print("data")
print(data)
print(data.shape)

# make a figure + axes
fig, ax = plt.subplots(1, 1, tight_layout=True)
# make color map
my_cmap = matplotlib.colors.ListedColormap(['aqua', 'g', 'b'])
# set the 'bad' values (nan) to be white and transparent
my_cmap.set_bad(color='w', alpha=0)
# draw the grid
for row in range(data.shape[0]):
    ax.axhline(row, lw=1.1, color='k', zorder=5)
for col in range(data.shape[1]):
    ax.axvline(col, lw=1.1, color='k', zorder=5)
# draw the boxes
ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, data.shape[1], 0, data.shape[0]], zorder=0)
# plot points
row_i = test_parameters[:, 0]
col_i = test_parameters[:, 1]
ax.plot(col_i - 0.5, data.shape[0] - row_i + 0.5, "ko", label="point")
ax.plot(test_parameters[:, 0] - 0.5, data.shape[0] - test_parameters[:, 0] + 0.5, "go", label="point_diag")
ax.legend(loc=1)
# Prepare x-axis ticks-n-labels
ax.set_xlabel("Model Columns")
ax.set_xticks(np.arange(data.shape[1]) + 0.5)
ax.set_xticklabels(np.arange(1, data.shape[1]+1))
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')
# Prepare y-axis ticks-n-labels
ax.set_ylabel("Model Rows")
ax.set_yticks(np.arange(data.shape[0]) + 0.5)
ax.set_yticklabels(np.arange(1, data.shape[0]+1)[::-1])

plt.show()
# fig.savefig("Figure1.pdf")
