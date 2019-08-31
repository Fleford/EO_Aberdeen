import numpy as np
from GWM_Manipulator_abr import read_fitness_array, write_abr_decvar, write_abr_hedcon, run_gwm
from GWM_Manipulator_abr import extract_rivercells, extract_wellcells
from GWM_Manipulator_abr import save_new_solution, save_best_solution, load_recent_solution
from scipy.optimize import differential_evolution
import time

# Initial variables and parameters
objfnc_eval_count = 0
list_of_bests_save_file = "list_of_bests_DE_abr.tsv"
start_time = time.time()


def n_nearest_dist(d, x, n):
    # Determines 2nd shortest distance to point of interest
    # D = set of points, x = point of interest
    # Each row is a point
    # euclidean distances from the other points
    sqd = np.linalg.norm(d - x, axis=1)
    idx = np.argsort(sqd)  # sorting
    # return the distance to the nearest neighbor
    return sqd[idx[n]]


def make_solution_matrix(input_index_parameter_matrix, input_fitness):
    # Build new solution matrix, set fitness ready flag, and increment counter
    input_fitness = input_fitness.reshape(-1, 1)
    return np.append(input_index_parameter_matrix, input_fitness, axis=1)


def objfnc(x):
    global best_totalfitness
    global best_index_parameter_matrix
    global objfnc_eval_count

    # Convert input into index_parameter_matrix
    x = np.asarray(x).round()
    parameter_matrix = x.reshape(-1, 2)
    index_matrix = np.arange(1, len(parameter_matrix)+1).reshape(-1, 1)
    index_parameter_matrix = np.concatenate((index_matrix, parameter_matrix), axis=1)

    # Prepare avoided points (River Cells)
    well_cells = extract_wellcells()
    river_cells = extract_rivercells()
    wells_and_river_cells = np.concatenate((well_cells, river_cells), axis=0)

    # Check if wells satisfy constraints. Return zero if they do not
    for well in parameter_matrix:
        # Check if the well is too close to a river or pre-existing well
        if n_nearest_dist(wells_and_river_cells, well, 0) < 1.0:
            return 0
        # Check if the well is too close to another well:
        if n_nearest_dist(parameter_matrix, well, 1) < 1.0:
            return 0

    # Prepare new GWM files using the index-parameter matrix
    write_abr_decvar(index_parameter_matrix)
    write_abr_hedcon(index_parameter_matrix)

    # Run GWM
    # print("Running gwm on: ", x, end="  ")
    try:
        run_gwm()
    except:
        print("Error with run_gwm")
        return 0

    # Increment evaluation counter
    objfnc_eval_count += 1

    # Define ordered list of wells
    wells = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]

    # Read in the new fitness vector and return the negative sum
    fitness_array = read_fitness_array(wells)
    totalfitness = -fitness_array.sum().round()

    # print("fitness: ", totalfitness, end="  ")

    # Save best solution
    if totalfitness < -best_totalfitness:
        best_totalfitness = -totalfitness
        best_index_parameter_matrix = index_parameter_matrix
        save_best_solution(make_solution_matrix(index_parameter_matrix, fitness_array), objfnc_eval_count)

    # Save solutions to text
    save_new_solution(make_solution_matrix(index_parameter_matrix, fitness_array), objfnc_eval_count)

    print("best_totalfitness")
    print(best_totalfitness)
    print("best_index_parameter_matrix")
    print(best_index_parameter_matrix)

    # Save fitness to text
    with open(list_of_bests_save_file, "a+") as write_best_totalfitness:
        write_best_totalfitness.write(str(best_totalfitness) + "\t")

    # Report time
    print("Time since start in seconds: " + str(time.time() - start_time))

    return totalfitness


# test = np.array([[15, 4],
#                  [11, 22],
#                  [18, 29],
#                  [18, 29]])
# test1 = [12, 11, 16, 17, 11, 22, 14, 25]
# test2 = [15, 4, 11, 22, 18, 29, 5, 18]
# print(objfnc(test1))
# print(objfnc(test2))

model_bounds = [(100, 300), (100, 300),
                (100, 300), (100, 300),
                (100, 300), (100, 300),
                (100, 300), (100, 300),
                (100, 300), (100, 300),
                (100, 300), (100, 300)]

for runs in range(1):
    best_solution = np.zeros(len(model_bounds))
    best_totalfitness = 0
    list_of_best_fitness = []
    result = differential_evolution(objfnc, model_bounds, disp=True, maxiter=10, polish=False, popsize=4)
    # np.savetxt('DE_Supply2_Best.out', best_solution, delimiter=',')
    print("DONE! result.x:{} ,result.fun:{}".format(result.x, result.fun))
    print("Final runtime in seconds: " + str(time.time() - start_time))

    # Save the list of best fitness to a text file
    with open(list_of_bests_save_file, "a+") as write_newline:
        write_newline.write("\n")

