from GWM_Manipulator import read_fitness_array, write_supply2decvar, run_gwm, extract_rivercells
from EO_PointTest.EO import EO, generate_initial_array, nearest_dist
import numpy as np
import matplotlib.pyplot as plt

# Test GWM_Manipulator functions
test_parameters = np.array([[1, 12, 11], # Index, Row, Column
                            [2, 16, 17],
                            [4, 14, 25]])
write_supply2decvar(test_parameters)
# run_gwm()
print()
print("Resulting fitness:")
wells = ["Q1", "Q2", "Q4"]
print(read_fitness_array(wells))
print()
print("extract_rivercells")
avoided_points = extract_rivercells()
print(avoided_points)

# Test EO functions
# NOTICE: for EO, x is model row and y is model column
sol1 = EO(n_rows=3, x_min=2, x_max=24, y_min=1, y_max=30, avoid_list=avoided_points)
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
ax.plot(avoided_points[:, 1], avoided_points[:, 0], "bs", markersize=12)
# Plot wells
ax.plot(sol1.solution[:, 2], sol1.solution[:, 1], 'ro')
plt.axis([1, 30, 25, 1])
plt.show()
