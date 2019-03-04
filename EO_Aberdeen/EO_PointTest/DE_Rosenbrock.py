import numpy as np
from scipy.optimize import differential_evolution


def rosenbrock_multi_2d(x_array):
    # Prep variables for best
    global best_fitness
    global list_of_best_fitness

    x_array = np.asarray(x_array)
    x_array = x_array.reshape(-1, 2)

    def rosenbrock_2d(x, y, a=1, b=100):
        # Minimum at
        return (a - x) ** 2 + b * (y - x ** 2) ** 2

    result = sum(rosenbrock_2d(x_array[:, 0], x_array[:, 1]))

    # Save best
    if result < best_fitness:
        best_fitness = result
    # print(best_fitness)
    list_of_best_fitness.append(best_fitness)

    return result


n_points = 10
model_bounds = [(-2, 4) for x in range(n_points*2)]
solution = np.ones(n_points*2)

for runs in range(100):
    print("Run: " + str(runs))

    best_fitness = 10000000.0
    list_of_best_fitness = []

    result = differential_evolution(rosenbrock_multi_2d, model_bounds, disp=False, maxiter=10, polish=False, popsize=10)
    print("DONE! result.x:{} ,result.fun:{}".format(result.x, result.fun))
    print(list_of_best_fitness)
    print(len(list_of_best_fitness))

    # Save the list of best fitness to a text file
    with open("list_of_bests_DE_rosenbrock.tsv", "a+") as write_f:
        for value in list_of_best_fitness:
            s = str(value)
            # Just write without the decimals
            write_f.write(s[:s.index('.')] + "\t")
        write_f.write("\n")
