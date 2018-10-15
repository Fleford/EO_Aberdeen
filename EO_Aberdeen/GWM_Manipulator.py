import subprocess

import numpy as np


def extract_contributions():
    # Looks at the GWM out file and extracts well names and contributions

    start_string1 = "OPTIMAL RATES FOR EACH FLOW VARIABLE"
    start_string2 = "Q1"
    end_string = "------------        ------------        ------------"
    # starter_string = "Q1    "
    line_cnt = 0
    start_string1_flag = False
    print_flag = False

    well_array_contributions = np.array([])
    well_array_names = []

    with open("supply2.gwmout.parallel", 'r') as f:

        for line in f:
            line_cnt = line_cnt + 1

            # Look for when the optimal solution table starts and stops
            if start_string1 in line:
                start_string1_flag = True
            if start_string1_flag and start_string2 in line:
                print_flag = True
            elif end_string in line:
                print_flag = False
                start_string1_flag = False

            # Split line into an array
            line_array = line.split()

            # Extract Contributions from "Contribution to objective"
            if print_flag:
                well_array_contributions = np.append(well_array_contributions, np.array([float(line_array[2])]), axis=0)

            # Extract names of well index_and_parameters_matrix
            if print_flag:
                well_array_names.append(line_array[0])

    return well_array_names, well_array_contributions


def search_string_in_array(searched_string, string_array):
    # Checks a list of strings if a certain string is found
    # Returns an array of ones and zeros

    found_array = np.array([])
    for name in string_array:
        if searched_string in name:
            found_array = np.append(found_array, np.array([1]))
        else:
            found_array = np.append(found_array, np.array([0]))

    return found_array

# # Tests extract_contributions, search_string_in_array and dot product method
# well_names, well_contributions = extract_contributions()
# print(well_names)
# print(well_contributions.reshape(-1, 1))
# found = search_string_in_array("Q2", well_names)
# print(found)
# print(well_contributions.dot(found))


def well_name(well_number, stress_period):
    # Outputs a formatted string given a well number and a stress period
    return "Q"+str(well_number)+"S"+str(stress_period)+"P"


def well_name_xy(well_x, well_y, stress_period):
    # Outputs a formatted string given well coordinates and a stress period
    return "X"+str(well_x)+"Y"+str(well_y)+"S"+str(stress_period)+"P"

# # Tests well_name, well_name_xy
# print(well_name(2, 39))
# print(well_name_xy(25, 30, 45))


def read_fitness_array(list_of_well_names):
    # Given a list of well names, the corresponding fitness array is produced
    well_names_with_sp, well_contributions = extract_contributions()
    fitness = np.array([])

    for well in list_of_well_names:
        found = search_string_in_array(well, well_names_with_sp)
        fitness = np.append(fitness, np.array([well_contributions.dot(found)]), axis=0)

    return fitness

# # Tests read_fitness_array
# wells = ["Q1", "Q2", "Q4"]
# print(read_fitness_array(wells))


def write_supply2decvar(index_and_parameters_matrix):
    # A function (or functions) that can output a decvar file using a template, provided an index-parameter array
    # The index array is in included with the index_and_parameters_matrix

    # Sort parameter rows by the index matrix
    index_and_parameters_matrix = index_and_parameters_matrix[index_and_parameters_matrix[:, 0].argsort()]

    # Recast matrix as dtype = int
    index_and_parameters_matrix = index_and_parameters_matrix.astype(int)

    with open("supply2.decvartp", "r") as read_f:
        with open("supply2.decvar", "w") as write_f:
            for line in read_f:

                # Insert new data
                # When adding new wells, PAY ATTENTION TO WHAT INDEXES ARE USED!!!
                if "Q1" in line:
                    xx = str(index_and_parameters_matrix[0, 1])
                    yy = str(index_and_parameters_matrix[0, 2])
                    # print(line.replace("xx", xx).replace("yy", yy), end="")
                    new_line = line.replace("xx", xx).replace("yy", yy)
                elif "Q2" in line:
                    xx = str(index_and_parameters_matrix[1, 1])
                    yy = str(index_and_parameters_matrix[1, 2])
                    # print(line.replace("xx", xx).replace("yy", yy), end="")
                    new_line = line.replace("xx", xx).replace("yy", yy)
                elif "Q3" in line:
                    xx = str(index_and_parameters_matrix[2, 1])
                    yy = str(index_and_parameters_matrix[2, 2])
                    # print(line.replace("xx", xx).replace("yy", yy), end="")
                    new_line = line.replace("xx", xx).replace("yy", yy)
                elif "Q4" in line:
                    xx = str(index_and_parameters_matrix[3, 1])
                    yy = str(index_and_parameters_matrix[3, 2])
                    # print(line.replace("xx", xx).replace("yy", yy), end="")
                    new_line = line.replace("xx", xx).replace("yy", yy)
                else:
                    new_line = line

                # Write new line to file
                write_f.write(new_line)


def write_supply2hedcon(index_and_parameters_matrix):
    # A function (or functions) that can output a hedcon file using a template, provided an index-parameter array
    # The index array is in included with the index_and_parameters_matrix

    # Sort parameter rows by the index matrix
    index_and_parameters_matrix = index_and_parameters_matrix[index_and_parameters_matrix[:, 0].argsort()]

    # Recast matrix as dtype = int
    index_and_parameters_matrix = index_and_parameters_matrix.astype(int)

    with open("supply2.hedcontp", "r") as read_f:
        with open("supply2.hedcon", "w") as write_f:
            for line in read_f:

                # Insert new data
                # When adding new wells, PAY ATTENTION TO WHAT INDEXES ARE USED!!!
                if "Q1" in line:
                    xx = str(index_and_parameters_matrix[0, 1])
                    yy = str(index_and_parameters_matrix[0, 2])
                    # print(line.replace("xx", xx).replace("yy", yy), end="")
                    new_line = line.replace("xx", xx).replace("yy", yy)
                elif "Q2" in line:
                    xx = str(index_and_parameters_matrix[1, 1])
                    yy = str(index_and_parameters_matrix[1, 2])
                    # print(line.replace("xx", xx).replace("yy", yy), end="")
                    new_line = line.replace("xx", xx).replace("yy", yy)
                elif "Q3" in line:
                    xx = str(index_and_parameters_matrix[2, 1])
                    yy = str(index_and_parameters_matrix[2, 2])
                    # print(line.replace("xx", xx).replace("yy", yy), end="")
                    new_line = line.replace("xx", xx).replace("yy", yy)
                elif "Q4" in line:
                    xx = str(index_and_parameters_matrix[3, 1])
                    yy = str(index_and_parameters_matrix[3, 2])
                    # print(line.replace("xx", xx).replace("yy", yy), end="")
                    new_line = line.replace("xx", xx).replace("yy", yy)
                else:
                    new_line = line

                # Write new line to file
                write_f.write(new_line)

# # Tests the write_supply2decvar and write_supply2hedcon
# test_parameters = np.array([[1, 12, 11],
#                             [2, 16, 17],
#                             [4, 14, 25]])
# write_supply2decvar(test_parameters)
# write_supply2hedcon(test_parameters)


def run_gwm():
    # Write a function that runs GWM with new local files and updates local files to be ready for use
    # Use stdout=subprocess.PIPE to keep subprocess.run quiet

    # print()
    # print("Copying over new files to GWM directory...")
    subprocess.run(r".\Batch_Files\copy_to_gwm", stdout=subprocess.PIPE, shell=True)
    # subprocess.run(r".\Batch_Files\copy_to_gwm", stdout=subprocess.PIPE, shell=True)

    # print()
    # print("Running GWM...")
    # proc = subprocess.run(r".\Batch_Files\start_gwm", encoding='utf-8', stdout=subprocess.PIPE, shell=True)
    # for line in proc.stdout.split('\n'):
    #     print(line)
    subprocess.run(r".\Batch_Files\start_gwm", stdout=subprocess.PIPE, shell=True)
    # subprocess.run(r".\Batch_Files\start_gwm", shell=True)
    # remove " stdout=subprocess.PIPE," to print output of subprocess

    # print()
    # print("Copying over resulting files from GWM directory...")
    subprocess.run(r".\Batch_Files\copy_from_gwm", stdout=subprocess.PIPE, shell=True)

    # print()

# # Tests run_gwm
# test_parameters = np.array([[1, 12, 11], # Index, Row, Column
#                             [2, 16, 17],
#                             [4, 14, 25]])
# write_supply2decvar(test_parameters)
# run_gwm()
# print()
# print("Resulting fitness:")
# wells = ["Q1", "Q2", "Q4"]
# print(read_fitness_array(wells))


def extract_rivercells():
    # Write a function that loads the river cells from *.sfr file into an array
    # Input is the directory of the river cell file
    # Output is an array, where each row is a point, [row, col]
    # Note: Duplicate cells are NOT removed

    line_cnt = 0
    n_cells = 0
    river_cells = []
    with open("supply2.sfr", "r") as f:
        for line in f:
            line_array = line.split()

            # Ignore start of file comments marked by "#"
            if line_array[0] == "#":
                continue

            # Start counting lines of data
            line_cnt = line_cnt + 1

            # Grab number of lines of data of from the first line
            if line_cnt == 1:
                n_cells = int(line_array[0])

            # Grab data from lines in range of n_cells
            if 1 < line_cnt <= n_cells + 1:
                row = int(line_array[1])
                col = int(line_array[2])
                river_cells.append([row, col])

    # Convert to numpy array
    river_cells = np.asanyarray(river_cells)

    # Gimme da good stuff
    return river_cells

# # Tests extract_rivercells
# print(extract_rivercells())
#
# # Prepare plot instance for extract_rivercells
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# ax.plot(extract_rivercells()[:, 1], extract_rivercells()[:, 0], "bs", markersize=12)
# plt.axis([1, 30, 25, 1])
# plt.show()


