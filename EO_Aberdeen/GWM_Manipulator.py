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

            # Extract names of well parameters
            if print_flag:
                well_array_names.append(line_array[0])

    return well_array_names, well_array_contributions


well_names, well_contributions = extract_contributions()
print(well_names)
print()
print(well_contributions)


# Combine well names with contribution values ?
