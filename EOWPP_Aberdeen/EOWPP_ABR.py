import matplotlib.pyplot as plt
import numpy as np

# Working directory set to C:\Users\Fleford\PycharmProjects\EO_Aberdeen\EOWPP_Aberdeen
from EOWPP_GWModel import EO, generate_possible_point, generate_initial_array
from GWM_Manipulator_abr import read_fitness_array, write_abr_decvar, write_abr_hedcon, run_gwm
from GWM_Manipulator_abr import extract_rivercells, extract_wellcells

# # Test GWM_Manipulator functions
# test_parameters = np.array([[1, 150, 200],    # Index, Row, Column
#                             [2, 140, 210],
#                             [3, 130, 220],
#                             [4, 120, 230],
#                             [5, 110, 240],
#                             [6, 100, 250]])
# write_abr_decvar(test_parameters)
# run_gwm()
# print()
# print("Resulting fitness:")
# wells = ["Q1", "Q2", "Q4"]
# print(read_fitness_array(wells))
# print()

print("extract_wellcells")
well_cells = extract_wellcells()
print(well_cells)
print()
print("extract_rivercells")
river_cells = extract_rivercells()
print(river_cells)
print()
print("Combining river and well cell lists")
wells_and_river_cells = np.concatenate((well_cells, river_cells), axis=0)
print(wells_and_river_cells)

# Test EO functions
# NOTICE: for EO, x is model row and y is model column
# sol1 = EO(n_rows=6, x_min=2, x_max=367, y_min=2, y_max=409, avoid_list=wells_and_river_cells, min_dist=3)
sol1 = EO(n_rows=6, x_min=30, x_max=300, y_min=30, y_max=300, avoid_list=wells_and_river_cells, min_dist=3)
initial_solution = np.array([[1, 106, 225, 0],
                             [2, 117, 174, 0],
                             [3, 101, 205, 0],
                             [4, 153, 222, 0],
                             [5, 114, 240, 0],
                             [6, 109, 202, 0]])
sol1.solution = initial_solution
print()
print(sol1.solution)
print(sol1.fitness_ready)
print(sol1.min_dist)
print()

# Testing Plots
# Prepare plot instance for extract_rivercells
# NOTICE: for plotting, x is columns, y is rows
fig, ax = plt.subplots()
# Plot river
ax.plot(river_cells[:, 1], river_cells[:, 0], "b,")
# Plot wells
ax.plot(sol1.solution[:, 2], sol1.solution[:, 1], 'r.')
plt.axis([1, 410, 368, 1])  # [y_min - 1, y_max + 1, x_max + 1, x_min - 1]
plt.show()


# # Prepare avoided points
# well_cells = extract_wellcells()
# river_cells = extract_rivercells()
# wells_and_river_cells = np.concatenate((well_cells, river_cells), axis=0)
#
# # Prepare EO instance
# sol1 = EO(n_rows=6, x_min=30, x_max=300, y_min=30, y_max=300, avoid_list=wells_and_river_cells, min_dist=3)
#
# # Load in initial parameters
# initial_solution = np.array([[1, 251, 290, 0],
#                              [2, 126, 121, 0],
#                              [3, 229, 199, 0],
#                              [4, 231, 218, 0],
#                              [5, 186, 247, 0],
#                              [6, 107, 178, 0]])
# sol1.solution = initial_solution
#
#
# def update_fitness_matrix(self):
#     # Parse out index-parameter matrix
#     index_parameter_matrix = np.delete(self.solution, 3, 1)
#
#     # Prepare new GWM files using the index-parameter matrix
#     write_abr_decvar(index_parameter_matrix)
#     write_abr_hedcon(index_parameter_matrix)
#
#     # Run GWM
#     run_gwm()
#
#     # Define ordered list of wells
#     wells = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]
#
#     # Sort solution matrix by index (same as ordered list of wells)
#     self.sort_index()
#
#     # Read in the new fitness vector and apply it to the solution matrix
#     self.update_fitness(read_fitness_array(wells))
#
#
# def plot_result(x=0):
#     print("Plotting the result")
#     print()
#     ax.clear()
#     ax.plot(river_cells[:, 1], river_cells[:, 0], "b,")  # Col, row
#     ax.plot(sol1.solution[:, 2], sol1.solution[:, 1], "g.")
#     # Label weakest and pivot well
#     sol1.sort_fitness()
#     ax.plot(sol1.solution[0, 2], sol1.solution[0, 1], "r.")     # weakest well
#     ax.plot(sol1.solution[-1, 2], sol1.solution[-1, 1], "b.")   # pivot well
#     # Annotate well names
#     for i, txt in enumerate(sol1.solution[:, 0]):
#         ax.annotate(txt, (sol1.solution[i, 2], sol1.solution[i, 1]))
#     ax.set_title("Iteration = {}, Fitness = {}".format(x, sol1.total_fitness()))
#     plt.axis([1, 410, 368, 1])  # [y_min - 1, y_max + 1, x_max + 1, x_min - 1]
#     plt.pause(0.1)
#
#
# # Run through first iteration
# # Updates the solution matrix with new fitness values
#
# # Prepare plot instances
# fig, ax = plt.subplots()
#
# # Prepare empty list for best fitness
# list_of_best_fitness = []
#
# # Update the fitness matrix (first run)
# print("Initial Parameters")
# print("sol1.solution")
# print(sol1.solution)
# print("sol1.fitness_ready? " + str(sol1.fitness_ready))
# print()
# print("Plotting initial solution:")
# print()
# plot_result()
#
# print("Running update_fitness_matrix(sol1):")
# update_fitness_matrix(sol1)
# print()
# print("After update_fitness_matrix(sol1):")
# print("sol1.solution")
# print(sol1.solution)
# print("sol1.fitness_ready? " + str(sol1.fitness_ready))
# print("Running sol1.update_best()")
# sol1.update_best()
# print(sol1.best_solution.solution)
# print("sol1.best_solution.total_fitness()")
# print(sol1.best_solution.total_fitness())
# list_of_best_fitness.append(sol1.best_solution.total_fitness())
# print()
# print("Plotting new solution:")
# print()
# plot_result()
#
# # Start of loop
# # Based on results, generate a new parameter matrix
# num_of_loops = 128
# for iteration in range(1, num_of_loops + 1):
#     print("Remove weakest")
#     sol1.remove_weakest()
#     print(sol1.solution)
#     print()
#
#     print("Generate and Append a new row")
#     sol1.append_row(sol1.generate_row())
#     print(sol1.solution)
#     print("sol1.fitness_ready? " + str(sol1.fitness_ready))
#     print()
#
#     print("update_fitness_matrix(sol1) with new parameter data")
#     update_fitness_matrix(sol1)
#     print("sol1.solution")
#     print(sol1.solution)
#     print("sol1.fitness_ready? " + str(sol1.fitness_ready))
#     print("sol1.fitness = " + str(sol1.total_fitness()))
#     print("Update Best")
#     sol1.update_best()
#     print(sol1.best_solution.solution)
#     print("sol1.best_solution.total_fitness()")
#     print(sol1.best_solution.total_fitness())
#     list_of_best_fitness.append(sol1.best_solution.total_fitness())
#     print()
#
#     plot_result(iteration)
#
#
# # Run GWM with best parameters
# print("Running gwm with best solution found")
# sol1.solution = sol1.best_solution.solution
# update_fitness_matrix(sol1)
# print("Plotting best solution found")
#
# plot_result()
#
# ax.set_title("Iteration = {}, Fitness = {}".format("Best", sol1.total_fitness()))
# plt.axis([1, 30, 25, 1])
# plt.pause(1000)
#
# # Show your hard work
# # plt.show()
# print("List of Best Fitness:")
# print(str(list_of_best_fitness))
#
# # # Save the best fitness to a text file
# # with open("list_of_bests", "a+") as write_f:
# #     for value in list_of_best_fitness:
# #         s = str(value)
# #         write_f.write(s[:s.index('.')] + "\t")
# #     write_f.write("\n")
#
# # Implement a write-to-textfile option
# # Implement annotated wells
# # Balance the weight of the wells
# # Implement drawdown constraints and K heterogeneity
# # Fix bug with repeating parameters
# # Compare EO with Best-outta-N-tries algorithm
