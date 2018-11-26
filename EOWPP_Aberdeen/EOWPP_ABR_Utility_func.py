import numpy as np


def check_ib(cell_row_col):
    # Returns true if the cell is active, else false
    # Input is a two-element np.array, [0] is row, [1] is col

    ib = np.loadtxt("ib2_ref.dat", dtype=bool)
    return ib[cell_row_col[0], cell_row_col[1]]

# # Test check_ib
# given_point = np.array([30, 30])
# print(check_ib(given_point))


# Extract river cells
def extract_rivercells():
    # Write a function that loads the river cells from *.sfr file into an array
    # Input is the directory of the river cell file
    # Output is an array, where each row is a point, [row, col]
    # Note: Duplicate cells are NOT removed

    line_cnt = 0
    n_cells = 0
    river_cells = []
    with open("abr_ref.sfr", "r") as f:
        for line in f:
            line_array = line.split()

            # Ignore if the string is empty
            if len(line_array) == 0:
                continue

            # Ignore start of file comments marked by "#"
            if line_array[0] == '#':
                continue

            # Start counting lines of data
            line_cnt = line_cnt + 1

            # Grab number of lines of data of from the first line
            if line_cnt == 1:
                n_cells = abs(int(line_array[0]))

            # Grab data from lines in range of n_cells
            if 1 < line_cnt <= n_cells + 1:
                row = int(line_array[1])
                col = int(line_array[2])
                river_cells.append([row, col])

    # Convert to numpy array
    river_cells = np.asanyarray(river_cells)

    # Gimme da good stuff
    return river_cells

# Tests extract_rivercells
print(extract_rivercells())
