import numpy as np
import copy

# git testing

class EOWellField(object):
    """
    Attributes:
        solution: A matrix that contains the component parameters and their fitness
        fitness_ready: A Boolean flag that's True if the fitness reflects the well parameters
        best_solution: The best solution found so far
        eval_count: Total number of times the fitness functions ran
        :return:
    """
    def __init__(self, n_rows=4, maximize=True):
        """
        Returns a EO_Solution object
        :return:
        """
        self.solution = np.random.rand(n_rows, 3)   # (row,col)
        self.fitness_ready = False
        self.best_solution = copy.deepcopy(self)
        self.eval_count = 0
        self.maximize = 1

        if not maximize:
            self.maximize = -1

    def parameters(self):
        """
        Returns the parameter matrix of the object
        :return:
        """
        # Parse out parameter matrix
        solution_rows, solution_cols = self.solution.shape
        parameters = np.delete(self.solution, (solution_cols - 1), 1)
        return parameters

    def fitness(self):
        """
        Returns the fitness vector of the object
        :return:
        """
        # Parse out fitness vector
        fitness = self.solution[:, (self.solution.shape[1]-1)]
        return fitness

    def update_fitness(self):
        """
        Modifies the solution matrix with the updated fitness
        :return:
        """
        # Parse out parameter matrix
        parameters = self.parameters()

        # Generate new fitness vector
        fitness = np.linalg.norm(parameters, axis=1)*self.maximize

        # Build new solution matrix, set fitness ready flag, and increment counter
        self.solution = np.c_[parameters, fitness]
        self.fitness_ready = True
        self.eval_count += 1

        # Sort solution matrix by fitness
        self.sort_fitness()

    def check_fitness(self):
        """
        Returns an error if the fitness vector does not reflect the parameter matrix
        :return:
        """
        # Check if the fitness is ready
        if not self.fitness_ready:
            print("The fitness vector does not reflect the parameter matrix!")

    def sort_fitness(self):
        """
        Modifies the solution matrix with rows sorted by fitness,
        with the first row having the lowest fitness
        :return:
        """
        # Check fitness if it's ready
        self.check_fitness()

        # Sort the solution matrix by fitness
        self.solution = self.solution[np.argsort(self.solution[:, self.solution.shape[1] - 1])]

    def remove_weakest(self):
        """
        Modifies the solution matrix with the rows of lowest fitness removed.
        At least the lowest fitness row is removed.
        :return:
        """
        self.solution = np.delete(self.solution, 0, 0)

    def generate_row(self):
        """
        Use the least fit row of the parameter matrix to return a new row for the parameter matrix
        :return:
        """
        # Parse out parameter matrix and dimensions
        parameters = self.parameters()
        parameters_rows, parameters_cols = parameters.shape

        # Get a random distance between two unique and random points
        n1 = np.random.randint(parameters_rows)
        n2 = (n1 + np.random.randint(low=1, high=parameters_rows)) % parameters_rows
        r1 = parameters[n1]
        r2 = parameters[n2]
        rand_dist = np.linalg.norm(r2 - r1)

        # Get a random unit vector
        u = np.random.rand(2) - np.array([0.5, 0.5])
        u = u / np.linalg.norm(u)

        # Scale random unit vector by the rand_dist
        u = rand_dist * u

        # Generate a new point using lowest fit row
        new_point = parameters[0] + np.random.rand() * u

        # Return a new row with right dimensions for the solution matrix
        return np.append(new_point, np.zeros(1))

    def append_row(self, new_row):
        """
        Modifies the solution matrix with a new row inserted
        :return:
        """
        # Modify solution with new row
        self.solution = np.append([new_row], self.solution, axis=0)

        # Assume the new addition has no fitness
        self.fitness_ready = False

    def total_fitness(self):
        """
        Returns the overall fitness for the solution
        :return:
        """
        # Check fitness if it's ready
        self.check_fitness()

        # Return the total fitness
        return np.sum(self.fitness())

    def update_best(self):
        """
        Updates the best solution if the new solution surpasses the current best solution
        :return:
        """
        # The first best solution is a valid solution
        if self.eval_count == 1:
            self.best_solution = copy.deepcopy(self)

        # Update best solution
        if self.total_fitness() >= self.best_solution.total_fitness():
            self.best_solution = copy.deepcopy(self)

    def iterate(self):
        """
        Runs through an iteration of the EO process. Assumes a preexisting valid solution matrix
        :return:
        """
        # Check if it's the first time
        if self.eval_count == 0:
            self.update_fitness()
            self.update_best()

        # Otherwise, run through an iteration
        else:
            self.remove_weakest()
            self.append_row(self.generate_row())
            self.update_fitness()
            self.update_best()


# Testing the EO_Solution class

sol1 = EOWellField(5, False)
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
