import numpy as np
import matplotlib.colors as colors
import matplotlib.pyplot as plt
from EO_Aberdeen.EO_PointTest import EO


def rosenbrock_2d(x, y, a=1, b=100):
    # Minimum at
    return (a - x) ** 2 + b * (y - x ** 2) ** 2


def rosensbrock_multi_2d(x_array):
    x_array = np.asarray(x_array)
    x_array = x_array.reshape(-1, 2)

    def rosenbrock_2d(x, y, a=1, b=100):
        # Minimum at
        return (a - x) ** 2 + b * (y - x ** 2) ** 2

    return sum(rosenbrock_2d(x_array[:, 0], x_array[:, 1]))


def calculate_fitness(self, sf):
    # Parse out parameter matrix
    parameters = self.parameters()/sf

    # Generate new fitness vector
    fitness = rosenbrock_2d(parameters[:, 0], parameters[:, 1])

    return fitness


def plot_result(points, itr):
    # global point_plot

    # Clear image
    plt.cla()

    CS = ax.pcolormesh(X, Y, Z, norm=colors.LogNorm(vmin=Z.min(), vmax=Z.max()), cmap="plasma")
    # cbar = fig.colorbar(CS)
    cbar.ax.get_yaxis().labelpad = 15
    cbar.ax.set_ylabel('2D Rastrigin Local Fitness', rotation=270)

    # Plot global min and points
    ax.plot(1, 1, "co", label="Global minimum", markeredgecolor="white", markersize=8)
    ax.plot(points[:, 0], points[:, 1], "b^", label="Current solution", markeredgecolor="white", markersize=8)
    ax.set_title("Iteration = {}, Total Fitness = {}".format(itr, round(sol1.total_fitness())))
    ax.legend(loc=2)

    fig.savefig(str(itr) + ".png", bbox_inches='tight', dpi=300)

    # plt.pause(0.1)


# Prepare figure instance
fig, ax = plt.subplots()

# Prepare background map math
X = np.linspace(-2, 4, 400)
Y = np.linspace(-2, 4, 400)
X, Y = np.meshgrid(X, Y)
pairs = np.stack([X.reshape(-1), Y.reshape(-1)]).T
Z = rosensbrock_multi_2d(np.stack([X.reshape(-1), Y.reshape(-1)]).T)
Z = np.asarray([rosensbrock_multi_2d(x) for x in pairs])
Z = Z.reshape(X.shape)
CS = ax.pcolormesh(X, Y, Z, norm=colors.LogNorm(vmin=Z.min(), vmax=Z.max()), cmap="plasma")
cbar = fig.colorbar(CS)
cbar.ax.get_yaxis().labelpad = 10
cbar.ax.set_ylabel('2D Rosenbrock Local Fitness', rotation=270)

n_points = 10
min = -2
max = 4
# Note that coordinates are scaled to increase resolution
scale = 1000

for runs in range(100):
    print("Run: " + str(runs))
    best_fitness = 1000
    list_of_best_fitness = []
    sol1 = EO.EO(n_rows=n_points, maximize=False, x_min=min*scale, x_max=max*scale, y_min=min*scale, y_max=max*scale,
                 min_dist=1)
    sol1.update_fitness(calculate_fitness(sol1, scale))
    sol1.update_best()
    list_of_best_fitness.append(sol1.best_solution.total_fitness())
    # print(sol1.best_solution.total_fitness())

    for iteration in range(100):
        sol1.remove_weakest()
        sol1.append_row(sol1.generate_row())
        sol1.update_fitness(calculate_fitness(sol1, scale))
        sol1.update_best()
        list_of_best_fitness.append(sol1.best_solution.total_fitness())
        print(iteration)
        print(sol1.best_solution.total_fitness())
        print(sol1.best_solution.parameters() / scale)

        # Save pdf of current solution
        plot_result(sol1.parameters() / scale, iteration)

    # Stop running when a better solution is found
    if sol1.best_solution.total_fitness() < 6:
        print("NEW RECORD")
        print(sol1.best_solution.total_fitness())
        break

    # # Save the list of best fitness to a text file
    # print(list_of_best_fitness)
    # print(list_of_best_fitness[-1])
    # print(len(list_of_best_fitness))
    # with open("list_of_bests_EOWPP_rosenbrock.tsv", "a+") as write_f:
    #     for value in list_of_best_fitness:
    #         s = str(value)
    #         # Just write without the decimals
    #         write_f.write(s[:s.index('.')] + "\t")
    #     write_f.write("\n")

# np.savetxt("EO_Aberdeen/EO_PointTest/Benchmark_samples/EOWPP_Rosenbrock1.txt", sol1.best_solution.parameters()/scale)
