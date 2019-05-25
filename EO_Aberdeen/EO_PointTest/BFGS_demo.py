import numpy as np
from scipy.optimize import minimize
# fun = lambda x: (x[0] - 1)**2 + (x[1] - 2.5)**2


# def fun(x):
#     result = (x[0])**2 + (x[1])**2 + (x[2])**2 + (x[3])**2
#     print(x, result)
#     return result


def cone_2d(x, y):
    # It's basically the Euclidean distance from the origin
    return np.sqrt(x ** 2 + y ** 2)


def cone_multi_2d_total(x_array):
    x_array = np.asarray(x_array)
    x_array = x_array.reshape(-1, 2)

    result = sum(cone_2d(x_array[:, 0], x_array[:, 1]))

    print(result)

    return result

# cons = ({'type': 'ineq', 'fun': lambda x:  x[0] - 2 * x[1] + 2},
#         {'type': 'ineq', 'fun': lambda x: -x[0] - 2 * x[1] + 6},
#         {'type': 'ineq', 'fun': lambda x: -x[0] + 2 * x[1] + 2})

# bnds = ((2, 10), (2, 10))

initial_guess = np.array([-100, 10, -100, 100, -100, 100, -100, 100, -100, 100])
maxiter = 125
res = minimize(cone_multi_2d_total, initial_guess, method='BFGS', options={'disp': True, 'maxiter': 10})

print(res.x)
print(res.fun)
