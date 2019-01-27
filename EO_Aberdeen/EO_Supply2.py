import matplotlib.pyplot as plt
import numpy as np

from EO_PointTest.EO import EO
from GWM_Manipulator import read_fitness_array, write_supply2decvar, write_supply2hedcon, run_gwm, extract_rivercells

# # Test GWM_Manipulator functions
# test_parameters = np.array([[1, 12, 11], # Index, Row, Column
#                             [2, 16, 17],
#                             [4, 14, 25]])
# write_supply2decvar(test_parameters)
# run_gwm()
# print()
# print("Resulting fitness:")
# wells = ["Q1", "Q2", "Q4"]
# print(read_fitness_array(wells))
# print()
# print("extract_rivercells")
# avoided_points = extract_rivercells()
# print(avoided_points)
#
# # Test EO functions
# # NOTICE: for EO, x is model row and y is model column
# sol1 = EO(n_rows=3, x_min=2, x_max=24, y_min=2, y_max=29, avoid_list=avoided_points)
# print()
# print(sol1.solution)
# print(sol1.fitness_ready)
# print(sol1.min_dist)
# print()
#
# # Testing Plots
# # Prepare plot instance for extract_rivercells
# # NOTICE: for plotting, x is columns, y is rows
# fig, ax = plt.subplots()
# # Plot river
# ax.plot(avoided_points[:, 1], avoided_points[:, 0], "bs", markersize=12)
# # Plot wells
# ax.plot(sol1.solution[:, 2], sol1.solution[:, 1], 'ro')
# plt.axis([1, 30, 25, 1])  # [y_min - 1, y_max + 1, x_max + 1, x_min - 1]
# plt.show()


# Prepare avoided points (River Cells)
rivercells = extract_rivercells()

# Prepare EO instance
sol1 = EO(n_rows=4, x_min=3, x_max=23, y_min=2, y_max=29, avoid_list=rivercells, min_dist=1)

# Rename index values
sol1.solution[0, 0] = 1
sol1.solution[1, 0] = 2
sol1.solution[2, 0] = 3
sol1.solution[3, 0] = 4

# Load in initial parameters
initial_solution = np.array([[1, 12, 11, 0],  # Index, Row, Column
                             [2, 16, 17, 0],
                             [3, 11, 22, 0],
                             [4, 14, 25, 0]])
# sol1.solution = initial_solution


def update_fitness_matrix(self):
    # Parse out index-parameter matrix
    index_parameter_matrix = np.delete(self.solution, 3, 1)

    # Prepare new GWM files using the index-parameter matrix
    write_supply2decvar(index_parameter_matrix)
    write_supply2hedcon(index_parameter_matrix)

    # Run GWM
    run_gwm()

    # Define ordered list of wells
    wells = ["Q1", "Q2", "Q3", "Q4"]

    # Sort solution matrix by index (same as ordered list of wells)
    self.sort_index()

    # Read in the new fitness vector and apply it to the solution matrix
    self.update_fitness(read_fitness_array(wells))

    # Convert the index-parameter part of the solution matrix into ints
    # (USELESS since np array must be in one datatype)
    # print(self.solution)
    # index_parameter_matrix = np.delete(self.solution, 3, 1).astype(int)
    # fitness_matrix = self.fitness().reshape(-1, 1)
    # print(index_parameter_matrix)
    # print(fitness_matrix)
    # self.solution = np.append(index_parameter_matrix, fitness_matrix, axis=1)
    # print(self.solution)


def plot_result(x=0):
    print("Plotting the result")
    print()
    ax.clear()
    ax.plot(rivercells[:, 1], rivercells[:, 0], "bs", markersize=12)  # Col, row
    ax.plot(sol1.solution[:, 2], sol1.solution[:, 1], "go")
    # Label weakest and pivot well
    sol1.sort_fitness()
    ax.plot(sol1.solution[0, 2], sol1.solution[0, 1], "ro")
    ax.plot(sol1.solution[-1, 2], sol1.solution[-1, 1], "bo")

    # Uncomment to save figures
    fig.savefig(str(x) + ".pdf", bbox_inches='tight')

    # Annotate well names
    for i, txt in enumerate(sol1.solution[:, 0]):
        ax.annotate(txt, (sol1.solution[i, 2], sol1.solution[i, 1]))
    ax.set_title("Iteration = {}, Fitness = {}".format(x, sol1.total_fitness()))
    plt.axis([1, 30, 25, 1])
    plt.pause(0.1)


# Run through first iteration
# Updates the solution matrix with new fitness values

# Prepare plot instances
fig, ax = plt.subplots()

# Prepare empty list for best fitness
list_of_best_fitness = []

# Update the fitness matrix (first run)
print("Initial Parameters")
print("sol1.solution")
print(sol1.solution)
print("sol1.fitness_ready? " + str(sol1.fitness_ready))
print()

print("After update_fitness_matrix(sol1):")
update_fitness_matrix(sol1)
print("sol1.solution")
print(sol1.solution)
print("sol1.fitness_ready? " + str(sol1.fitness_ready))
print("Update Best")
sol1.update_best()
print(sol1.best_solution.solution)
print("sol1.best_solution.total_fitness()")
print(sol1.best_solution.total_fitness())
list_of_best_fitness.append(sol1.best_solution.total_fitness())
print()

plot_result()

# Start of loop
# Based on results, generate a new parameter matrix
num_of_loops = 20
for iteration in range(1, num_of_loops + 1):
    print("Remove weakest")
    sol1.remove_weakest()
    print(sol1.solution)
    print()

    print("Generate and Append a new row")
    sol1.append_row(sol1.generate_row())
    print(sol1.solution)
    print("sol1.fitness_ready? " + str(sol1.fitness_ready))
    print()

    print("update_fitness_matrix(sol1) with new parameter data")
    update_fitness_matrix(sol1)
    print("sol1.solution")
    print(sol1.solution)
    print("sol1.fitness_ready? " + str(sol1.fitness_ready))
    print("sol1.fitness = " + str(sol1.total_fitness()))
    print("Update Best")
    sol1.update_best()
    print(sol1.best_solution.solution)
    print("sol1.best_solution.total_fitness()")
    print(sol1.best_solution.total_fitness())
    list_of_best_fitness.append(sol1.best_solution.total_fitness())
    print()

    plot_result(iteration)


# Run GWM with best parameters
print("Running gwm with best solution found")
sol1.solution = sol1.best_solution.solution
update_fitness_matrix(sol1)
print("Plotting best solution found")

plot_result()

ax.set_title("Iteration = {}, Fitness = {}".format("Best", sol1.total_fitness()))
plt.axis([1, 30, 25, 1])
plt.pause(1000)

# Show your hard work
# plt.show()
print("List of Best Fitness:")
print(str(list_of_best_fitness))

# # Save the best fitness to a text file
# with open("list_of_bests", "a+") as write_f:
#     for value in list_of_best_fitness:
#         s = str(value)
#         write_f.write(s[:s.index('.')] + "\t")
#     write_f.write("\n")

# Implement a write-to-textfile option
# Implement annotated wells
# Balance the weight of the wells
# Implement drawdown constraints and K heterogeneity
# Fix bug with repeating parameters
# Compare EO with Best-outta-N-tries algorithm
