import copy

import numpy as np


class EO(object):
    """
    Attributes:
        solution: A matrix that contains the component parameters and their fitness
        fitness_ready: A Boolean flag that's True if the fitness reflects the well parameters
        best_solution: The best solution found so far
        eval_count: Total number of times the fitness functions ran
        :return:
    """

    def __init__(self, n_rows=4, maximize=True, x_min=0, x_max=100, y_min=0, y_max=100, min_dist=2,
                 avoid_list=np.array([[]])):
        """
        Returns a EO_Solution object
        :return:
        """
        self.solution = np.random.rand(n_rows, 4)  # np.random.rand(row,col)
        self.replaced_row_index = 0
        self.replaced_row_parameter = np.array([])
        self.fitness_ready = False
        self.best_solution = copy.deepcopy(self)
        self.eval_count = 0
        self.maximize = 1
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.min_dist = min_dist
        self.avoid_list = avoid_list

        if self.avoid_list.shape[1] == 0:
            print("No avoid list provided")

        # Set to maximizing or minimizing
        if not maximize:
            self.maximize = -1

        # Initialize the solution matrix with valid parameters
        parameter_matrix = generate_initial_array(x_min, x_max, y_min, y_max, n_rows, min_dist, avoid_list)
        zero_vector = np.zeros(n_rows).reshape(-1, 1)
        self.solution = np.append(parameter_matrix, zero_vector, axis=1)

        # Append index matrix to left of solution matrix
        index_array = np.arange(n_rows).reshape(-1, 1)
        self.solution = np.append(index_array, self.solution, axis=1)

    def parameters(self):
        """
        Returns the parameter matrix of the object
        :return:
        """
        # Parse out parameter matrix
        solution_rows, solution_cols = self.solution.shape
        parameters = np.delete(self.solution, (solution_cols - 1), 1)   # Remove fitness matrix
        parameters = np.delete(parameters, 0, 1)    # Remove index matrix
        return parameters

    def fitness(self):
        """
        Returns the fitness vector of the object
        :return:
        """
        # Parse out fitness vector
        fitness = self.solution[:, (self.solution.shape[1] - 1)]
        return fitness

    def update_fitness(self, fitness):
        """
        Modifies the solution matrix with the updated fitness.
        Adds a given fitness vector the solution matrix
        :return:
        """

        # Build new solution matrix, set fitness ready flag, and increment counter
        fitness = fitness.reshape(-1, 1)
        self.solution = np.delete(self.solution, -1, 1)
        self.solution = np.append(self.solution, fitness, axis=1)
        self.fitness_ready = True
        self.eval_count += 1

        # Sort solution matrix by fitness
        # self.sort_fitness()

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

    def sort_index(self):
        """
        Modifies the solution matrix with rows sorted by index matrix value,
        with the first row having the smallest index value
        :return:
        """
        # Sort the solution matrix by fitness
        self.solution = self.solution[np.argsort(self.solution[:, 0])]

    def remove_weakest(self):
        """
        Modifies the solution matrix with the rows of lowest fitness removed.
        At least the lowest fitness row is removed.
        :return:
        """
        # Sort solution matrix by fitness first
        self.sort_fitness()

        # Save the index and parameter of the row to be removed
        self.replaced_row_index = self.solution[0, 0]   # [row, col]
        self.replaced_row_parameter = self.solution[0, 1:3]

        # Remove row
        self.solution = np.delete(self.solution, 0, 0)

    def generate_parameter(self):
        """
        Uses the parameter matrix to return a new random parameter
        :return:
        """
        # Sort solution matrix by fitness (first row = weakest fitness)
        self.sort_fitness()

        # Parse out parameter matrix and dimensions
        parameters = self.parameters()
        parameters_rows, parameters_cols = parameters.shape

        # # Get a random distance between two unique and random points
        # n1 = np.random.randint(parameters_rows)
        # # n1 = -1  # Pivot from the best point
        # n2 = (n1 + np.random.randint(low=1, high=parameters_rows)) % parameters_rows
        # r1 = parameters[n1]
        # r2 = parameters[n2]
        # placement_radius = np.linalg.norm(r2 - r1)

        # Use the maximal distance as the placement radius
        placement_radius = maximal_dist(parameters)

        # Get a random unit vector
        u = np.random.rand(2) - np.array([0.5, 0.5])
        u = u / np.linalg.norm(u)

        # Scale random unit vector by the placement_radius
        u = placement_radius * u

        # Return a new point using lowest fit row, [0], most fit = [-1]
        new_point = parameters[-1] + np.random.rand() * u * 1
        # new_point = parameters[np.random.randint(parameters_rows)] + np.random.rand() * u

        # Clip new point to boundary and round components
        new_point = condition_vector(new_point, self.x_min, self.x_max, self.y_min, self.y_max)

        # Return new parameter
        return new_point

    def check_constraints(self, checked_parameter):
        """
        Returns true if the checked_parameter respects all constraints
        :return:
        """
        # Check if it's too close to other points
        dist_flag = check_dist_constraint(checked_parameter, self.parameters(), self.min_dist, self.avoid_list)

        # Check if it's the same as the removed row parameter
        repeat_flag = not np.array_equal(self.replaced_row_parameter, checked_parameter)

        return dist_flag and repeat_flag

    def generate_row(self):
        """
        Use the least fit row of the parameter matrix to return a new valid row for the parameter matrix
        :return:
        """
        # Keep making new parameters until you find something valid
        new_parameter = self.generate_parameter()
        while not self.check_constraints(new_parameter):
            new_parameter = self.generate_parameter()

        # Attach the index of the replaced parameter
        new_parameter = np.append(np.array(self.replaced_row_index), new_parameter)

        # Return a new row with right dimensions for the solution matrix
        return np.append(new_parameter, np.zeros(1))

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


def nearest_dist(d, x):
    # Determines shortest distance to point of interest
    # D = set of points, x = point of interest
    # Each row is a point
    # euclidean distances from the other points
    sqd = np.linalg.norm(d - x, axis=1)
    idx = np.argsort(sqd)  # sorting
    # return the distance to the nearest neighbor
    return sqd[idx[0]]


def farthest_dist(d, x):
    # Determines farthest distance to point of interest
    # D = set of points, x = point of interest
    # Each row is a point
    # euclidean distances from the other points
    sqd = np.linalg.norm(d - x, axis=1)
    idx = np.argsort(sqd)  # sorting
    # return the distance to the nearest neighbor
    return sqd[idx[-1]]


def maximal_dist(d):
    # Determines the largest distance possible between two points of a set of points
    # D = set of points
    # Each row is a point
    # euclidean distances from the other points
    maximum_distance = 0.0
    for point in d:
        test_distance = farthest_dist(d, point)
        if test_distance >= maximum_distance:
            maximum_distance = test_distance
    return maximum_distance


def check_dist_constraint(given_point, array_of_points, min_dist, avoid_list=np.array([[]])):
    # Returns true if the given point is greater than or equal to the minimum distance away from the closest point
    # Each row is an x,y  point

    # Check for an avoid list
    if avoid_list.shape[1] == 0:
        print("No avoid list provided for check_dist_constraint")
        array_of_points_all = array_of_points
    else:
        # Include avoid list into array of checked points
        array_of_points_all = np.append(array_of_points, avoid_list, axis=0)

    return nearest_dist(array_of_points_all, given_point) >= min_dist


def generate_possible_point(x_min, x_max, y_min, y_max):
    # Generates a random point within broadest model bounds, inclusive
    # New point is of whole numbers, no decimals

    # Generate random x and y point that are within bounds
    x_new_point = np.random.randint(low=x_min, high=x_max + 1)
    y_new_point = np.random.randint(low=y_min, high=y_max + 1)

    # Stitch into a row vector and return array
    return np.array([x_new_point, y_new_point])


def generate_initial_array(x_min, x_max, y_min, y_max, n_rows, min_dist, avoid_list=np.array([[]])):
    # Generates the first parameter array with n_rows = number of rows
    # All points are within bounds
    # All points are a minimum distance from each other

    # Check for an avoid list
    if avoid_list.shape[1] == 0:
        print("No avoid list provided for generate_initial_array ")
        initial_array = np.array([generate_possible_point(x_min, x_max, y_min, y_max)])
    else:
        # Generates an initial, valid array
        initial_array = np.array([generate_possible_point(x_min, x_max, y_min, y_max)])
        while not nearest_dist(avoid_list, initial_array[0]) >= min_dist:
            initial_array = np.array([generate_possible_point(x_min, x_max, y_min, y_max)])

    # Generate an initial test point
    new_point = generate_possible_point(x_min, x_max, y_min, y_max)

    # Generate the rest of the points
    for i in range(0, n_rows - 1):
        # Generate valid point
        while not check_dist_constraint(new_point, initial_array, min_dist, avoid_list):
            new_point = generate_possible_point(x_min, x_max, y_min, y_max)

        # Append new point to array
        initial_array = np.append([new_point], initial_array, axis=0)

    # Give me what I want
    return initial_array


def condition_vector(given_point, x_min, x_max, y_min, y_max):
    # Clips given point to provided bounds then rounds all components

    # Clip point to bounds
    given_point[0] = given_point[0].clip(x_min, x_max)
    given_point[1] = given_point[1].clip(y_min, y_max)

    # Round components to whole numbers
    return given_point.round()
