import math
import numpy as np
import matplotlib.pyplot as plt
from EO_Aberdeen.EO_PointTest import EO


def rastrigin(x, a=10):
    x = np.asarray(x)
    x = np.clip(x, -5.12, 5.12)
    n = len(x)

    # Minimum when inputs are 0
    def rastrigin_sum_term(xi):
        return xi ** 2 - a * np.cos(2 * math.pi * xi)

    totalfitness = a * n + sum(rastrigin_sum_term(x))

    return totalfitness


def calculate_fitness(self, sf):
    # Parse out parameter matrix
    parameters = self.parameters()/sf

    # Generate new fitness vector
    fitness = rastrigin([parameters[:, 0], parameters[:, 1]])

    return fitness


def plot_result(points, itr):
    # global point_plot

    # Clear image
    plt.cla()

    # Prepare background map
    # X = np.linspace(-5.12, 5.12, 700)
    # Y = np.linspace(-5.12, 5.12, 700)
    # X, Y = np.meshgrid(X, Y)
    # Z = rastrigin([X.reshape(-1), Y.reshape(-1)], a=10)
    # Z = Z.reshape(X.shape)
    CS = ax.pcolormesh(X, Y, Z, cmap="plasma")
    # cbar = fig.colorbar(CS)
    cbar.ax.get_yaxis().labelpad = 15
    cbar.ax.set_ylabel('2D Rastrigin Local Fitness', rotation=270)

    # Plot global min and points
    ax.plot(0, 0, "co", label="Global minimum", markeredgecolor="white", markersize=8)
    ax.plot(points[:, 0], points[:, 1], "b^", label="Current solution", markeredgecolor="white", markersize=8)
    ax.set_title("Iteration = {}, Total Fitness = {}".format(itr, round(sol1.total_fitness())))
    ax.legend(loc=2)

    fig.savefig(str(itr) + ".png", bbox_inches='tight', dpi=300)

    # plt.pause(0.1)


# Prepare figure instance
fig, ax = plt.subplots()

# Prepare background map math
X = np.linspace(-5.12, 5.12, 700)
Y = np.linspace(-5.12, 5.12, 700)
X, Y = np.meshgrid(X, Y)
Z = rastrigin([X.reshape(-1), Y.reshape(-1)], a=10)
Z = Z.reshape(X.shape)
CS = ax.pcolormesh(X, Y, Z, cmap="plasma")
cbar = fig.colorbar(CS)
cbar.ax.get_yaxis().labelpad = 15
cbar.ax.set_ylabel('2D Rastrigin Local Fitness', rotation=270)

n_points = 10
min = -5.12
max = 5.12
# Note that coordinates are scaled to increase resolution
scale = 1000

for runs in range(100):
    print("Run: " + str(runs))
    list_of_best_fitness = []
    sol1 = EO.EO(n_rows=n_points, maximize=False, x_min=min*scale, x_max=max*scale, y_min=min*scale, y_max=max*scale,
                 min_dist=1)

    sol1.update_fitness(calculate_fitness(sol1, scale))
    sol1.update_best()
    list_of_best_fitness.append(sol1.best_solution.total_fitness())
    # print(sol1.best_solution.total_fitness())

    # points = sol1.parameters()/scale
    # ax.plot(0, 0, "co", label="Global minimum", markeredgecolor="white", markersize=8)
    # point_plot = ax.plot(points[:, 0], points[:, 1], "b^", label="Current solution", markeredgecolor="white",
    #                      markersize=8)
    # ax.legend(loc=2)

    for iteration in range(100):
        sol1.remove_weakest()
        sol1.append_row(sol1.generate_row())
        sol1.update_fitness(calculate_fitness(sol1, scale))
        sol1.update_best()
        list_of_best_fitness.append(sol1.best_solution.total_fitness())
        print(iteration)
        print(sol1.best_solution.total_fitness())
        print(sol1.best_solution.parameters()/scale)

        # plt.clf()
        plot_result(sol1.parameters()/scale, iteration)
        # points = sol1.parameters() / scale
        # plt.cla()
        # CS = ax.pcolormesh(X, Y, Z, cmap="plasma")
        # point_plot = ax.plot(points[:, 0], points[:, 1], "b^", label="Current solution", markeredgecolor="white",
        #                      markersize=8)
        # ax.set_title("Iteration = {}, Total Fitness = {}".format(iteration, round(sol1.total_fitness())))
        # plt.pause(1)

    # Stop running when a better solution is found
    if sol1.best_solution.total_fitness() < 55:
        print("NEW RECORD")
        print(sol1.best_solution.total_fitness())
        break

    # # Save the list of best fitness to a text file
    # # print(len(list_of_best_fitness))
    # with open("list_of_bests_EOWPP_rastrigin_clip.tsv", "a+") as write_f:
    #     for value in list_of_best_fitness:
    #         s = str(value)
    #         # Just write without the decimals
    #         write_f.write(s[:s.index('.')] + "\t")
    #     write_f.write("\n")
# np.savetxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/EOWPP_Rastrigin1.txt", sol1.best_solution.parameters()/scale)
