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

# # Calculate fitness matrix
def calculate_fitness(self):
    # Parse out index-parameter matrix
    index_parameter_matrix = np.delete(sol1.solution, 3, 1)

    # Prepare new GWM files using the index-parameter matrix
    write_supply2decvar(index_parameter_matrix)

    # Run GWM
    run_gwm()

    # Define ordered list of wells
    wells = ["Q1", "Q2", "Q4"]

    # Sort solution matrix by index (same as ordered list of wells)
    self.sort_index()

    # Read in data and return a new fitness vector
    return read_fitness_array(wells)

# Update the solution matrix
print(sol1.solution)
print(sol1.fitness_ready)
sol1.update_fitness(calculate_fitness(sol1))
print(sol1.solution)
print(sol1.fitness_ready)
sol1.sort_index()
print(sol1.solution)

# Generate new fitness vector
# center_point = np.array([50, 50])
# fitness = np.linalg.norm(parameters - center_point, axis=1) * self.maximize