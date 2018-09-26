from GWM_Manipulator import read_fitness_array, write_supply2decvar, run_gwm, extract_rivercells
from EO_PointTest.EO import EO
import numpy as np
import matplotlib.pyplot as plt

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
# plt.axis([1, 30, 25, 1])
# plt.show()


# Prepare avoided points (River Cells)
rivercells = extract_rivercells()

# Prepare EO instance
sol1 = EO(n_rows=3, x_min=2, x_max=24, y_min=2, y_max=29, avoid_list=rivercells)

# Rename index values
sol1.solution[0, 0] = 1
sol1.solution[1, 0] = 2
sol1.solution[2, 0] = 4


# Updates the solution matrix with new fitness values
def update_fitness_matrix(self):
    # Parse out index-parameter matrix
    index_parameter_matrix = np.delete(self.solution, 3, 1)

    # Prepare new GWM files using the index-parameter matrix
    write_supply2decvar(index_parameter_matrix)

    # Run GWM
    # run_gwm()

    # Define ordered list of wells
    wells = ["Q1", "Q2", "Q4"]

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


# Update the fitness matrix (first run)
print("sol1.solution")
print(sol1.solution)
print("sol1.fitness_ready? " + str(sol1.fitness_ready))
update_fitness_matrix(sol1)
print("After update_fitness_matrix(sol1):")
print("sol1.solution")
print(sol1.solution)
print("sol1.fitness_ready? " + str(sol1.fitness_ready))
print("Update Best")
sol1.update_best()
print(sol1.best_solution.solution)
print()

# Based on results, generate a new parameter matrix
print("Remove weakest")
sol1.remove_weakest()
print(sol1.solution)
