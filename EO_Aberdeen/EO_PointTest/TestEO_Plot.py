from EO_Aberdeen.EO_PointTest import EO
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


# Prepare avoided points
avoided_points = np.array([[50, 55],
                           [50, 60],
                           [50, 50]])

# Prepare EO instance
sol1 = EO.EO(10, False, min_dist=3, avoid_list=avoided_points)

# Prepare plot instance
fig, ax = plt.subplots()


def calculate_fitness(self):
    # Parse out parameter matrix
    parameters = self.parameters()

    # Generate new fitness vector
    center_point = np.array([50, 50])
    fitness = np.linalg.norm(parameters - center_point, axis=1) * self.maximize

    return fitness


def iterate(self):
    self.remove_weakest()
    self.append_row(self.generate_row())
    self.update_fitness(calculate_fitness(self))
    self.update_best()


# Iterates and plots EO
def update(i):
    # Iterate through EO
    iterate(sol1)

    # Plot result
    ax.clear()
    ax.plot(sol1.solution[:, 1], sol1.solution[:, 2], 'bs')
    ax.plot(sol1.avoid_list[:, 0], sol1.avoid_list[:, 1], 'rs')
    ax.set_title("Gen = {}, BestSum = {}".format(i, sol1.total_fitness()))
    plt.axis([0, 100, 0, 100])


# Animation
ani = animation.FuncAnimation(fig, update, interval=1)
plt.show()
