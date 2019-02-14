from pyswarm import pso

def banana(x):
    print("heck!")
    x1 = x[0]
    x2 = x[1]
    return x1**4 - 2*x2*x1**2 + x2**2 + x1**2 - 2*x1 + 5

def con(x):
    x1 = x[0]
    x2 = x[1]
    return [-(x1 + 0.25)**2 + 0.75*x2]

lb = [-3, -1]
ub = [2, 6]

xopt, fopt = pso(banana, lb, ub, f_ieqcons=con, maxiter=1, swarmsize=3)

print(xopt, fopt)