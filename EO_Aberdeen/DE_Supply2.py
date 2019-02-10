from scipy.optimize import rosen, differential_evolution
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

from EO_PointTest.EO import EO
from GWM_Manipulator import read_fitness_array, write_supply2decvar, write_supply2hedcon, run_gwm, extract_rivercells


def n_nearest_dist(d, x, n):
    # Determines 2nd shortest distance to point of interest
    # D = set of points, x = point of interest
    # Each row is a point
    # euclidean distances from the other points
    sqd = np.linalg.norm(d - x, axis=1)
    idx = np.argsort(sqd)  # sorting
    # return the distance to the nearest neighbor
    return sqd[idx[n]]


def objfnc(x):
    # Convert input into index_parameter_matrix
    x = np.asarray(x).round()
    parameter_matrix = x.reshape(-1, 2)
    index_matrix = np.arange(1, len(parameter_matrix)+1).reshape(-1, 1)
    index_parameter_matrix = np.concatenate((index_matrix, parameter_matrix), axis=1)

    # Prepare avoided points (River Cells)
    rivercells = extract_rivercells()

    # Check if wells satisfy constraints. Return zero if they do not
    for well in parameter_matrix:
        # Check if the well is too close to the river
        if n_nearest_dist(rivercells, well, 0) < 1.0:
            return 0
        # Check if the well is too close to another well:
        if n_nearest_dist(parameter_matrix, well, 1) < 1.0:
            return 0

    # Prepare new GWM files using the index-parameter matrix
    write_supply2decvar(index_parameter_matrix)
    write_supply2hedcon(index_parameter_matrix)

    # Run GWM
    print("Running gwm on: ", x, end="  ")
    run_gwm()

    # Define ordered list of wells
    wells = ["Q1", "Q2", "Q3", "Q4"]

    # Read in the new fitness vector and return the negative sum
    totalfitness = -read_fitness_array(wells).sum()
    print(totalfitness)
    return totalfitness


test = np.array([[15, 4],
                 [11, 22],
                 [18, 29],
                 [18, 29]])

test2 = [15, 4, 11, 22, 18, 29, 5, 18]
print(objfnc(test2))

# model_bounds = [(3, 23), (2, 29),
#                 (3, 23), (2, 29),
#                 (3, 23), (2, 29),
#                 (3, 23), (2, 29)]
# result = differential_evolution(objfnc, model_bounds, disp=True, maxiter=10, polish=False, popsize=4)
# print("DONE! result.x:{} ,result.fun:{}".format(result.x, result.fun))


