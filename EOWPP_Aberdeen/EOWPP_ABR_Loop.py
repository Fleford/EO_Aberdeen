import os
import numpy as np
from EOWPP import EO
from GWM_Manipulator_abr import read_fitness_array, write_abr_decvar, write_abr_hedcon, run_gwm
from GWM_Manipulator_abr import extract_rivercells, extract_wellcells
from GWM_Manipulator_abr import save_new_solution, save_best_solution, load_recent_solution


# Prepare avoided points
well_cells = extract_wellcells()
river_cells = extract_rivercells()
wells_and_river_cells = np.concatenate((well_cells, river_cells), axis=0)

# Prepare EO instance
sol1 = EO(n_rows=6, x_min=100, x_max=300, y_min=30, y_max=300, avoid_list=wells_and_river_cells, min_dist=3)

# # Load in initial parameters
# initial_solution = np.array([[1, 251, 290, 0],
#                              [2, 126, 121, 0],
#                              [3, 229, 199, 0],
#                              [4, 231, 218, 0],
#                              [5, 186, 247, 0],
#                              [6, 107, 178, 0]])
# sol1.solution = initial_solution


def update_fitness_matrix(self):
    # Parse out index-parameter matrix
    index_parameter_matrix = np.delete(self.solution, 3, 1)

    # Prepare new GWM files using the index-parameter matrix
    write_abr_decvar(index_parameter_matrix)
    write_abr_hedcon(index_parameter_matrix)

    # Run GWM
    run_gwm()

    # Define ordered list of wells
    wells = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]

    # Sort solution matrix by index (same as ordered list of wells)
    self.sort_index()

    # Read in the new fitness vector and apply it to the solution matrix
    self.update_fitness(read_fitness_array(wells))


# Run through first iteration (if previous data doesn't exist)
if not os.path.isfile("EOWPP_FILES\EOWPP.solutions"):
    # Update the fitness matrix (first run)
    print("Initial Parameters")
    print("sol1.solution")
    print(sol1.solution)
    print("sol1.fitness_ready? " + str(sol1.fitness_ready))
    print()
    print("Plotting initial solution:")
    print()

    print("Running update_fitness_matrix(sol1):")
    update_fitness_matrix(sol1)
    print()
    print("After update_fitness_matrix(sol1):")
    print("sol1.solution")
    print(sol1.solution)
    print("sol1.fitness_ready? " + str(sol1.fitness_ready))
    print("Running sol1.update_best()")
    sol1.update_best()
    print(sol1.best_solution.solution)
    print("sol1.best_solution.total_fitness()")
    print(sol1.best_solution.total_fitness())
    print()
    print("Saving New Solution")
    save_new_solution(sol1.solution, sol1.eval_count)
    print()
    print("Saving Best Solution")
    save_best_solution(sol1.best_solution.solution, sol1.eval_count)
    print()

# Start of loop
# Based on results, generate a new parameter matrix
num_of_loops = 100
for run in range(1, num_of_loops + 1):
    print("Load in previously saved solution")
    sol1.solution, sol1.eval_count = load_recent_solution()
    sol1.fitness_ready = True
    print("sol1.solution")
    print(sol1.solution)
    print("sol1.eval_count")
    print(sol1.eval_count)
    print()

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
    print()
    print("Saving New Solution")
    save_new_solution(sol1.solution, sol1.eval_count)
    print()
    print("Saving Best Solution")
    save_best_solution(sol1.best_solution.solution, sol1.eval_count)
    print()
