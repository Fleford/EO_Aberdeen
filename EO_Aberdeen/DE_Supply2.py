from scipy.optimize import rosen, differential_evolution
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

from EO_PointTest.EO import EO
from GWM_Manipulator import read_fitness_array, write_supply2decvar, write_supply2hedcon, run_gwm, extract_rivercells


def objfnc(x):
    # Convert input into index_parameter_matrix
    x = np.asarray(x).round()
    parameter_matrix = x.reshape(-1, 2)
    index_matrix = np.arange(1, len(parameter_matrix)+1).reshape(-1, 1)
    index_parameter_matrix = np.concatenate((index_matrix, parameter_matrix), axis=1)

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



# def ackley(x):
#     arg1 = -0.2 * np.sqrt(0.5 * (x[0] ** 2 + x[1] ** 2))
#     arg2 = 0.5 * (np.cos(2. * np.pi * x[0]) + np.cos(2. * np.pi * x[1]))
#     return -20. * np.exp(arg1) - np.exp(arg2) + 20. + np.e
#
#
# bounds = [(-5, 5), (-5, 5)]
# result = differential_evolution(ackley, bounds, disp=True, maxiter=20, polish=False)
# print(result.x, result.fun)

model_bounds = [(3, 23), (2, 29),
                (3, 23), (2, 29),
                (3, 23), (2, 29),
                (3, 23), (2, 29)]
result = differential_evolution(objfnc, model_bounds, disp=True, maxiter=1, polish=False, popsize=4)
print("DONE! result.x:{} ,result.fun:{}".format(result.x, result.fun))
