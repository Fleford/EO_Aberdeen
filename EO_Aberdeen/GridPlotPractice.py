import numpy as np
import matplotlib.pyplot as plt
import matplotlib


N = 15
# make an empty data set
data = np.ones((N, N)) * np.nan
# fill in some fake data
for j in range(3)[::-1]:
    data[N//2 - j : N//2 + j +1, N//2 - j : N//2 + j +1] = j
print("data")
print(data)
# make a figure + axes
fig, ax = plt.subplots(1, 1, tight_layout=True)
# make color map
my_cmap = matplotlib.colors.ListedColormap(['r', 'g', 'b'])
# set the 'bad' values (nan) to be white and transparent
my_cmap.set_bad(color='w', alpha=0)
# draw the grid
for x in range(N + 1):
    ax.axhline(x, lw=2, color='k', zorder=5)
    ax.axvline(x, lw=2, color='k', zorder=5)
# draw the boxes
ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)
# ax.plot(12, 6, "go")

# Prepare x-axis ticks-n-labels
ax.set_xlabel("Model Columns")
ax.set_xticks(np.arange(N) + 0.5)
ax.set_xticklabels(np.arange(1, N+1))
ax.xaxis.set_ticks_position('top')
ax.xaxis.set_label_position('top')

# Prepare y-axis ticks-n-labels
ax.set_ylabel("Model Rows")
ax.set_yticks(np.arange(N) + 0.5)
ax.set_yticklabels(np.arange(1, N+1)[::-1])

plt.show()
fig.savefig("Figure1.pdf")