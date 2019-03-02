import numpy as np

filepath = "list_of_bests_PSO_rastrigin.tsv"

# Find minimum run length
min_len = 0
with open(filepath, "r") as f:
    for i, line in enumerate(f):
        line_array = line.split()
        new = list(map(float, line_array))
        line_len = len(new)
        if min_len == 0 or line_len < min_len:
            min_len = line_len
print(min_len)

