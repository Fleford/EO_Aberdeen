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


def well_name(well_number, stress_period):
    # Outputs a formatted string given a well number and a stress period
    return "Q"+str(well_number)+"S"+str(stress_period)+"P"


def well_name_xy(well_x, well_y, stress_period):
    # Outputs a formatted string given well coordinates and a stress period
    return "X"+str(well_x)+"Y"+str(well_y)+"S"+str(stress_period)+"P"


# Remove comments to test the functions above
well_names, well_contributions = extract_contributions()
print(well_names)
print(well_contributions.reshape(-1, 1))
found = search_string_in_array("a", well_names)
print(found)
print(well_contributions.dot(found))
print(well_name(2, 39))
print(well_name_xy(25, 30, 45))




