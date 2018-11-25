from EOWPP_Aberdeen.EOWPP import EO, generate_possible_point, generate_initial_array
import numpy as np

avoided_points = np.array([[20, 20],
                           [80, 80],
                           [20, 80]])


def calculate_fitness(self):
    # Parse out parameter matrix
    parameters = self.parameters()

    # Generate new fitness vector
    center_point = np.array([50, 50])
    fitness = np.linalg.norm(parameters - center_point, axis=1) * self.maximize

    return fitness


def iterate(self):
    self.remove_weakest()
    self.append_row(self.generate_row())
    self.update_fitness(calculate_fitness(self))
    self.update_best()


# Testing the EO_Solution class
sol1 = EO(10, False, avoid_list=avoided_points)
print(sol1.solution)
print(sol1.fitness_ready)
print()

print("Update fitness")
sol1.update_fitness(calculate_fitness(sol1))
print(sol1.solution)
print(sol1.total_fitness())
print("Fitness ready?", sol1.fitness_ready)
print(sol1.eval_count)
print()

print("Best Sol")
sol1.update_best()
print(sol1.best_solution.solution)
print(sol1.best_solution.total_fitness())
print(sol1.best_solution.fitness_ready)
print()

print("remove_weakest")
sol1.remove_weakest()
print(sol1.solution)
print("Replaced row_index: ", sol1.replaced_row_index)
print("Replaced row_parameter: ", sol1.replaced_row_parameter)
print()

print("generate_row")
row = sol1.generate_row()
print(row)
print()

print("append_row")
sol1.append_row(row)
print(sol1.solution)
print(sol1.fitness_ready)
print(sol1.total_fitness())
print()

print("Update fitness")
sol1.update_fitness(calculate_fitness(sol1))
print(sol1.solution)
print(sol1.total_fitness())
print(sol1.fitness_ready)
print(sol1.eval_count)
print()

print("Best Sol")
sol1.update_best()
print(sol1.best_solution.solution)
print(sol1.best_solution.total_fitness())
print(sol1.best_solution.fitness_ready)
print()

iterate(sol1)
print(sol1.solution)
print(sol1.total_fitness())
print()

print("Testing generate_parameter")
print(sol1.generate_parameter())
print()

print("Testing generate_possible_point")
print(generate_possible_point(10, 100, 20, 100))
print()

print("Testing generate_initial_array")
print(generate_initial_array(20, 80, 20, 80, 10, 1, avoid_list=avoided_points))
print()
