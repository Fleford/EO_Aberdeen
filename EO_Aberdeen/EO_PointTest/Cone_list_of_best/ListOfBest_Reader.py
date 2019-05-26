import numpy as np

rootname = "BFGS_cone"

filepath = "list_of_bests_" + rootname + ".tsv"

# Find minimum run length
min_len = 0
with open(filepath, "r") as f:
    for i, line in enumerate(f):
        line_array = line.split()
        new = list(map(float, line_array))
        line_len = len(new)
        if min_len == 0 or line_len < min_len:
            min_len = line_len

# Import values into a matrix
# Values that exceed the minimum length are truncated
with open(filepath, "r") as f:
    runs = []
    for i, line in enumerate(f):
        line_array = line.split()
        new = list(map(float, line_array))
        run = np.array(new[0:min_len])
        runs.append(run)
runs_matrix = np.stack(runs)

# Extract Statistics from runs
firstQ = np.percentile(runs_matrix, 25, axis=0)
secondQ = np.percentile(runs_matrix, 50, axis=0)
thirdQ = np.percentile(runs_matrix, 75, axis=0)
allQ = np.stack([firstQ, secondQ, thirdQ])
allQ = allQ.T
print(allQ)
np.savetxt("quantiles_" + rootname + ".csv", allQ, delimiter=",")
