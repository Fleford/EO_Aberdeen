from EO_Aberdeen.EO_PointTest import EO_Test


# Testing the EO_Solution class
sol1 = EO_Test.EO(5, False)
print(sol1.solution)
print(sol1.fitness_ready)
print()

sol1.update_fitness()
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

sol1.remove_weakest()
print(sol1.solution)
print()

row = sol1.generate_row()
print(row)
print()

sol1.append_row(row)
print(sol1.solution)
print(sol1.fitness_ready)
print(sol1.total_fitness())
print()

sol1.update_fitness()
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

sol1.iterate()
print(sol1.solution)
print(sol1.total_fitness())
print()

print("Testing generate_possible_point")
print(EO_Test.generate_possible_point(10, 100, 20, 100))
