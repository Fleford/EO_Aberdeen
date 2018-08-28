from EO_Aberdeen.EO_PointTest import EO_Test
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Prepare EO instance
sol1 = EO_Test.EO(10, False)

# Prepare plot instance
fig, ax = plt.subplots()


# Iterates and plots EO
def update(i):
    # Iterate through EO
    sol1.iterate()

    # Plot result
    ax.clear()
    ax.plot(sol1.solution[:, 0], sol1.solution[:, 1], 'ro')
    ax.set_title("Gen = {}, BestSum = {}".format(i, sol1.total_fitness()))
    plt.axis([0, 1, 0, 1])


# Animation
ani = animation.FuncAnimation(fig, update, interval=1)
plt.show()
