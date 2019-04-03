import matplotlib.pyplot as plt
import numpy as np

pop_size = 11
y_lim = 100
x = np.arange(pop_size)
fitness = np.random.randint(low=1, high=y_lim, size=pop_size)
print(fitness)
print(np.argmin(fitness))
fitness[np.argmin(fitness)] = np.random.randint(low=1, high=y_lim)
print(fitness)

fig, ax = plt.subplots()

for run in range(30):

    # plot points
    ax.clear()
    bar_plot = plt.bar(x, fitness)
    plt.xticks(x)
    ax.set_ylim([0, y_lim])
    plt.xlabel("Solution Components")
    plt.ylabel("Fitness of component")
    plt.title('Iteration = {}, Total fitness = {}'.format(run, np.sum(fitness)))
    # plt.pause(0.1)

    # find min index
    min_index = np.argmin(fitness)

    # color lowest fitness and plot
    # bar_plot[(min_index - 1) % pop_size].set_color('r')
    bar_plot[min_index].set_color('r')
    # bar_plot[(min_index + 1) % pop_size].set_color('r')

    # plot result
    plt.pause(0.3)

    # Adjust fitness
    # fitness[(min_index - 1) % pop_size] = np.random.randint(low=1, high=y_lim)
    fitness[min_index] = np.random.randint(low=1, high=y_lim)
    # fitness[(min_index + 1) % pop_size] = np.random.randint(low=1, high=y_lim)
