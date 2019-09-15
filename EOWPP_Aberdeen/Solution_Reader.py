import matplotlib.pyplot as plt
import numpy as np

from EOWPP_GWModel import EO
from GWM_Manipulator_abr import extract_rivercells, extract_wellcells


def txt_to_array(filepath):
    try:
        return np.loadtxt(filepath)
    except ValueError:
        with open(filepath, "r") as read_f:
            with open("col_fixed_" + filepath, "w") as write_f:
                ncol = 0
                for i, line in enumerate(read_f):
                    line_array = line.split()
                    if i == 0:
                        ncol = len(line_array)
                    for val in line_array:
                        write_f.write("\t" + val)
                    if len(line_array) != ncol:
                        write_f.write("\n")
        return np.loadtxt("col_fixed_" + filepath)


def load_ith_solution(filepath, iteration):
    # loads the solution matrix with given iteration number

    line_start = 0
    extracted_solution_matrix = []

    # Find the file index of the iteration number
    with open(filepath, "r") as f:
        for i, line in enumerate(f):
            line_array = line.split()
            if (len(line_array) == 2) and (int(line_array[1]) == int(iteration)):
                line_start = i

    # Load in solution matrix
    with open(filepath, "r") as f:
        for i, line in enumerate(f):
            if (line_start + 3) <= i <= (line_start + 3 + 5):
                line_array = line.split()
                new = list(map(float, line_array))
                extracted_solution_matrix.append(new)
    extracted_solution_matrix = np.array(extracted_solution_matrix)

    return extracted_solution_matrix


def plot_result_with_k(array, new_filename, itr=0):
    print("Plotting the result")
    print()
    plt.imshow(array, cmap="jet", alpha=0.6)
    cbar = plt.colorbar()
    cbar.set_label('Horizontal Hydraulic Conductivity [ft/day]', rotation=270)
    plt.plot(river_cells[:, 1], river_cells[:, 0], "b,")  # Col, row
    # plt.plot(sol1.solution[:, 2], sol1.solution[:, 1], "bo")
    plt.plot(sol1.solution[:, 2], sol1.solution[:, 1], "b.")
    # Label weakest and pivot well
    sol1.sort_fitness()
    # plt.plot(sol1.solution[0, 2], sol1.solution[0, 1], "r.")     # weakest well
    # plt.plot(sol1.solution[-1, 2], sol1.solution[-1, 1], "b.")   # pivot well
    # Annotate well ranks (1 is the most fit
    for i, txt in enumerate(sol1.solution[:, 0]):
        rank = str(6 - i)
        plt.annotate(rank, (sol1.solution[i, 2], sol1.solution[i, 1]))
    plt.title("Total Output [ft$^3$/yr] = {}".format(sol1.total_fitness()))
    # plt.title("Iteration = {}, Total Output [ft$^3$/yr] = {}".format(itr, sol1.total_fitness()))
    plt.axis([1, 410, 368, 1])  # [y_min - 1, y_max + 1, x_max + 1, x_min - 1]
    #  Label axes
    plt.xlabel("Model Columns (1 cell = 200 ft)")
    plt.ylabel("Model Rows (1 cell = 200 ft)")
    # # Save image
    # plt.savefig(new_filename)
    # plt.savefig(new_filename, bbox_inches='tight', dpi=300)
    plt.show()


def plot_result():
    print("Plotting the result")
    print()
    ax.clear()
    ax.plot(river_cells[:, 1], river_cells[:, 0], "b,")  # Col, row
    ax.plot(sol1.solution[:, 2], sol1.solution[:, 1], "g.")
    # Label weakest and pivot well
    sol1.sort_fitness()
    ax.plot(sol1.solution[0, 2], sol1.solution[0, 1], "r.")     # weakest well
    ax.plot(sol1.solution[-1, 2], sol1.solution[-1, 1], "b.")   # pivot well
    # Annotate well ranks (1 is the most fit
    for i, txt in enumerate(sol1.solution[:, 0]):
        rank = str(6 - i)
        ax.annotate(rank, (sol1.solution[i, 2], sol1.solution[i, 1]))
    ax.set_title("Fitness = {}".format(sol1.total_fitness()))
    plt.axis([1, 410, 368, 1])  # [y_min - 1, y_max + 1, x_max + 1, x_min - 1]
    #  Label axes
    ax.set_xlabel("Model Columns")
    ax.set_ylabel("Model Rows")
    plt.show()


# Main Program
solution_file_path = "EOWPP_FILES\_12_2_2018_921_EOWPP.solutions"
# solution_file_path = "EOWPP_FILES\_12_2_2018_1023_EOWPP.solutions"
# solution_file_path = "EOWPP_FILES\EOWPP_best.solutions"
# best_solution_file_path = "EOWPP_FILES\_12_1_2018_EOWPP_best.solutions"
# best_solution_file_path = "EOWPP_FILES\_11_29_2018_EOWPP_best.solutions"
# best_solution_file_path = "EOWPP_FILES\_12_2_2018_921_EOWPP_best.solutions"
# best_solution_file_path = "EOWPP_FILES\_12_2_2018_1023_EOWPP_best.solutions"
best_solution_file_path = "EOWPP_ABR_results/Run1/EOWPP_best.solutions"

# Prepare avoided points
well_cells = extract_wellcells()
river_cells = extract_rivercells()
wells_and_river_cells = np.concatenate((well_cells, river_cells), axis=0)
sol1 = EO(n_rows=6, x_min=100, x_max=300, y_min=100, y_max=300, avoid_list=wells_and_river_cells, min_dist=3)
sol1.solution = load_ith_solution(best_solution_file_path, 151)
sol1.fitness_ready = True

# Uncomment when using plot_result()
fig, ax = plt.subplots()

print(sol1.solution)
print(sol1.total_fitness())

# plot_result()
hkx = txt_to_array("abr2_kx.txt")
mask = txt_to_array("ib2_ref.dat")
hkx_masked = np.ma.masked_where(mask == 0, hkx)
plot_result_with_k(hkx_masked, "_12_2_2018_1023_EOWPP_best_kx.pdf")

# # Save Pictures, Uncomment when using plot_result()
# fig.savefig("_12_2_2018_1023_EOWPP_best.pdf")

# # Loop through all solutions and print total fitness 102
# for i in range(1, 3):
#     sol1.solution = load_ith_solution(solution_file_path, i)
#     sol1.fitness_ready = True
#     index_filename = str(i) + ".pdf"
#     print(index_filename)
#     print(sol1.total_fitness())
#     plot_result()

# # Generate list_of_bests.tsv file
# # Save fitness to text
# for i in range(1, 300):
#     sol1.solution = load_ith_solution(best_solution_file_path, i)
#     with open("list_of_bests_EOWPP_best.tsv", "a+") as write_best_totalfitness:
#         write_best_totalfitness.write(str(sol1.total_fitness()) + "\t")

