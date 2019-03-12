import numpy as np
from GWM_Manipulator import read_fitness_array, write_supply2decvar, write_supply2hedcon, run_gwm, extract_rivercells
from pyswarm import pso


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
    global best_fitness
    global list_of_best_fitness

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
    # print("Running gwm on: ", x, end="  ")
    try:
        run_gwm()
    except:
        print("Error with run_gwm")
        return 0

    # Define ordered list of wells
    wells = ["Q1", "Q2", "Q3", "Q4"]

    # Read in the new fitness vector and return the negative sum
    totalfitness = -read_fitness_array(wells).sum().round()
    # print("fitness: ", totalfitness, end="  ")

    # Save best
    if totalfitness < -best_fitness:
        best_fitness = -totalfitness
    print(best_fitness)
    list_of_best_fitness.append(best_fitness)

    return totalfitness


lb = [3, 2,
      3, 2,
      3, 2,
      3, 2]
ub = [23, 29,
      23, 29,
      23, 29,
      23, 29]

for runs in range(100):
    best_fitness = 0
    list_of_best_fitness = []
    xopt, fopt = pso(objfnc, lb, ub, maxiter=20, swarmsize=10)
    print("DONE! xopt:{} ,fopt:{}".format(xopt, fopt))

    # Save the list of best fitness to a text file
    print(len(list_of_best_fitness))
    with open("list_of_bests_PSO.tsv", "a+") as write_f:
        for value in list_of_best_fitness:
            s = str(value)
            write_f.write(s[:s.index('.')] + "\t")
        write_f.write("\n")
