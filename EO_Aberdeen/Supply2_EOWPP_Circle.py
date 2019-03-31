import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import numpy as np
from GWM_Manipulator import extract_rivercells


def farthest_dist(d, x):
    # Determines farthest distance to point of interest
    # D = set of points, x = point of interest
    # Each row is a point
    # euclidean distances from the other points
    sqd = np.linalg.norm(d - x, axis=1)
    idx = np.argsort(sqd)  # sorting
    # return the distance to the nearest neighbor
    return sqd[idx[-1]]


def maximal_dist(d):
    # Determines the largest distance possible between two points of a set of points
    # D = set of points
    # Each row is a point
    # euclidean distances from the other points
    maximum_distance = 0.0
    for point in d:
        test_distance = farthest_dist(d, point)
        if test_distance >= maximum_distance:
            maximum_distance = test_distance
    return maximum_distance


# Wells
wells_EOWPP = np.array([[15, 19],   # Row, Column (Total Fitness = 53764)
                        [13, 27],
                        [10, 23],
                        [18, 26]])
# # Wells
# wells_EOWPP = np.array([[10, 23],   # Row, Column (Total Fitness = 53764)
#                         [15, 19],
#                         [13, 27],
#                         [18, 26]])
print(maximal_dist(wells_EOWPP))
# wells_PSO = np.array([[16, 28],  # Row, Column (Total Fitness = 45059)
#                      [15, 16],
#                      [18, 14],
#                      [8, 25]])
# wells_DE = np.array([[18, 28],  # Row, Column (Total Fitness = 42829)
#                      [4, 24],
#                      [9, 16],
#                      [19, 19]])

# # Streamflow Constraint
# strmflw_cnstrnt = np.array([[14, 14],
#                             [14, 21],
#                             [13, 23],
#                             [15, 26]])
# # Load in HK
# SynthK = np.loadtxt("SynthHeteroK.txt")
# print(SynthK, SynthK.shape)

# Setup empty grid model
data = np.ones((25, 30)) * np.nan  # Rows, Cols
# put river cells in matrix
rivercells = extract_rivercells()
for rivercell in rivercells:
    data[rivercell[0]-1, rivercell[1]-1] = 0
# print("data")
# print(data)
# print(data.shape)

# make a figure + axes
fig, ax = plt.subplots(1, 1, tight_layout=True, figsize=(8, 5.5))
# make color map
river_cmap = matplotlib.colors.ListedColormap(['aqua'])
hk_cmap = matplotlib.colors.ListedColormap(['r', 'b'])
# set the 'bad' values (nan) to be white and transparent
river_cmap.set_bad(color='w', alpha=0)
# # draw the grid
# for row in range(data.shape[0]):
#     ax.axhline(row, lw=1.1, color='k', zorder=5)
# for col in range(data.shape[1]):
#     ax.axvline(col, lw=1.1, color='k', zorder=5)

# plot the river cells and hk
# hk_im = ax.imshow(SynthK, cmap=hk_cmap, extent=[0, SynthK.shape[1], 0, SynthK.shape[0]], alpha=0.3)
ax.imshow(data, interpolation='none', cmap=river_cmap, extent=[0, data.shape[1], 0, data.shape[0]], zorder=0)
# # add colorbar for hk
# cbar = plt.colorbar(hk_im)
# cbar.ax.get_yaxis().set_ticks([])
# for j, lab in enumerate(['$50$', '$500$']):
#     cbar.ax.text(1.5, (j * 0.5) + 0.25, lab, ha='center', va='center', rotation=270)
# cbar.ax.get_yaxis().labelpad = 30
# cbar.ax.set_ylabel('Transmissivity [ft$^2$/day]', rotation=270)

# plot points
ax.plot([], [], color="aqua", marker="s", label="River cell", markersize=8, linestyle="None", markeredgecolor="k")

# plot line
best_index = 0
max_col = wells_EOWPP[2:4, 1] - 0.5
max_row = data.shape[0] - wells_EOWPP[2:4, 0] + 0.5
plt.plot(max_col, max_row, color='orange')  # max length line
plt.text(max_col[0] - 0.5, max_row[0] - 2.0, "Largest distance", fontsize=10, rotation=-70)\
    .set_path_effects([PathEffects.withStroke(linewidth=5, foreground='w')])
del_col = (wells_EOWPP[best_index, 1] - 0.5) - max_col[0]
del_row = (data.shape[0] - wells_EOWPP[best_index, 0] + 0.5) - max_row[0]
plt.plot(max_col + del_col, max_row + del_row, color='orange')  # shifted line

# plot intermediate wells
# ax.plot(wells_EOWPP[0, 1] - 0.5, data.shape[0] - wells_EOWPP[0, 0] + 0.5, "go")
# ax.plot(wells_EOWPP[1, 1] - 0.5, data.shape[0] - wells_EOWPP[1, 0] + 0.5, "go")
ax.plot(wells_EOWPP[2, 1] - 0.5, data.shape[0] - wells_EOWPP[2, 0] + 0.5, "go")
ax.plot(wells_EOWPP[3, 1] - 0.5, data.shape[0] - wells_EOWPP[3, 0] + 0.5, "go")

# mark best well
best_index = 0
ax.plot(wells_EOWPP[best_index, 1] - 0.5, data.shape[0] - wells_EOWPP[best_index, 0] + 0.5, "bo")
plt.text(wells_EOWPP[best_index, 1] - 0.5 - 2, data.shape[0] - wells_EOWPP[best_index, 0] + 0.5 + 0.5, "Best well", fontsize=9)

# mark worst well
worst_index = 1
ax.plot(wells_EOWPP[worst_index, 1] - 0.5, data.shape[0] - wells_EOWPP[worst_index, 0] + 0.5, "ro")
plt.text(wells_EOWPP[worst_index, 1] - 0.5 - 1, data.shape[0] - wells_EOWPP[worst_index, 0] + 0.5 - 1, "Worst well", fontsize=9)

# mark new well
ax.plot(15 - 0.5, data.shape[0] - 20 + 0.5, "go")
plt.text(15 - 0.5 - 1, data.shape[0] - 20 + 0.5 - 1, "New well", fontsize=9)

# plot a circle
circle_row = wells_EOWPP[best_index, 0]
circle_col = wells_EOWPP[best_index, 1]
circle_radius = maximal_dist(wells_EOWPP)
circleEdge = plt.Circle((circle_col - 0.5, data.shape[0] - circle_row + 0.5), circle_radius, edgecolor="darkorange", fill=None)
circleEdge.set_linestyle('dashed')
circleFill = plt.Circle((circle_col - 0.5, data.shape[0] - circle_row + 0.5), circle_radius, color="orange", alpha=0.2)
ax.add_artist(circleFill)
ax.add_artist(circleEdge)

# ax.plot(wells_PSO[:, 1] - 0.5, data.shape[0] - wells_PSO[:, 0] + 0.5, "go",
#         label="PSO Well field (Total Fitness = 45059)")
# ax.plot(wells_DE[:, 1] - 0.5, data.shape[0] - wells_DE[:, 0] + 0.5, "ro",
#         label="DE Well field (Total Fitness = 42829)")
# # add legend
# ax.legend(loc=2)
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
# fig.savefig("EOWPP_Supply2_Overall.pdf")
