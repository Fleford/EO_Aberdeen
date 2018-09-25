import GWM_Manipulator
from EO_SupplyTest.EO import EO

wells = ["Q1", "Q2", "Q4"]
print(GWM_Manipulator.read_fitness_array(wells))

sol1 = EO(10, False)
print(sol1.solution)
print(sol1.fitness_ready)
print()
