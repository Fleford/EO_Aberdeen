from GWM_Manipulator import read_fitness_array, write_supply2decvar, run_gwm
from EO_PointTest.EO import EO
import numpy as np

# Test GWM_Manipulator functions
test_parameters = np.array([[1, 12, 11], # Index, Row, Column
                            [2, 16, 17],
                            [4, 14, 25]])
write_supply2decvar(test_parameters)
run_gwm()
print()
print("Resulting fitness:")
wells = ["Q1", "Q2", "Q4"]
print(read_fitness_array(wells))

# Test EO functions
avoided_points = np.array([[20, 20],
                           [80, 80],
                           [20, 80]])
sol1 = EO(10, False, avoid_list=avoided_points)
print(sol1.solution)
print(sol1.fitness_ready)
print()
