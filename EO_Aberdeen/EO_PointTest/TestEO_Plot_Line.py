from EO_Aberdeen.EO_PointTest import EO
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


# Prepare avoided points
# avoided_points = np.array([[50, 60],
#                            [50, 55],
#                            [50, 50]])

# Prepare EO instance
# sol1 = EO.EO(4, False, min_dist=2, avoid_list=avoided_points)
sol1 = EO.EO(n_rows=6, maximize=False, x_min=-100, x_max=100, y_min=-100, y_max=100, min_dist=2)

# Prepare plot instance
fig, ax = plt.subplots()


def calculate_fitness(self):
    # Parse out parameter matrix
    parameters = self.parameters()

    # Generate new fitness vector
    center_point_1 = np.array([50, 50])
    center_point_2 = np.array([-50, -50])
    fitness_1 = np.linalg.norm(parameters - center_point_1, axis=1)
    fitness_2 = np.linalg.norm(parameters - center_point_2, axis=1)
    fitness = (fitness_1 + fitness_2)

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
    ax.plot(sol1.solution[:, 1], sol1.solution[:, 2], 'bo')
    # ax.plot(sol1.avoid_list[:, 0], sol1.avoid_list[:, 1], 'ro')
    # Plot center target points
    ax.plot(50, 50, 'ro')
    ax.plot(-50, -50, 'ro')
    ax.set_title("Iteration = {}, AverageFitness = {}".format(i, round(-1*sol1.total_fitness()/sol1.n_rows, 2)))
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    plt.axis([sol1.x_min, sol1.x_max, sol1.y_min, sol1.y_max])

    print(round(-1*sol1.total_fitness()/sol1.n_rows, 2))


# Animation
ani = animation.FuncAnimation(fig, update, interval=100)
plt.show()
