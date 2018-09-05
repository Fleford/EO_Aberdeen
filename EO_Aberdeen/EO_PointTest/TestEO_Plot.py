from EO_Aberdeen.EO_PointTest import EO_Test
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


# Prepare avoided points
avoided_points = np.array([[20, 20],
                           [80, 80],
                           [60, 60]])

# Prepare EO instance
sol1 = EO_Test.EO(100, False, min_dist=2, avoid_list=avoided_points)

# Prepare plot instance
fig, ax = plt.subplots()


# Iterates and plots EO
def update(i):
    # Iterate through EO
    sol1.iterate()

    # Plot result
    ax.clear()
    ax.plot(sol1.solution[:, 0], sol1.solution[:, 1], 'bo')
    ax.plot(sol1.avoid_list[:, 0], sol1.avoid_list[:, 1], 'ro')
    ax.set_title("Gen = {}, BestSum = {}".format(i, sol1.total_fitness()))
    plt.axis([0, 100, 0, 100])


# Animation
ani = animation.FuncAnimation(fig, update, interval=1)
plt.show()
