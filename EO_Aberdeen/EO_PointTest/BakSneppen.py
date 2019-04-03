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

ax.set_ylim([0, y_lim])
bar_plot = plt.bar(x, fitness)

plt.xticks(x)
plt.xlabel("Creatures")
plt.ylabel("Fitness of creature")
bar_plot[np.argmin(fitness)-1].set_color('r')
bar_plot[np.argmin(fitness)].set_color('r')
bar_plot[np.argmin(fitness)+1].set_color('r')

plt.pause(1)




ax.clear()
plt.pause(1)