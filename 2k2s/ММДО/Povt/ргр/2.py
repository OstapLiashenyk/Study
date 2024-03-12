import numpy as np

n, m = 3, 3



a = np.array([

    [9, 5, 0],

    [5, 3, 3],

    [2, 4, 6]

], dtype=float)



plan = np.array([200, 400, 90], dtype=float)

coefs = np.array([15, 8, 9], dtype=float)

basis_id = np.array([0, 1, 2], dtype=int)



max_iterations = 100

tolerance = 1e-5

for iteration_counter in range(max_iterations):

    print(f"Iteration {iteration_counter + 1}")

    reduced_costs = coefs - np.dot(coefs[basis_id], a)



    if np.all(reduced_costs <= tolerance):

        print("Optimal solution found.")

        break



    entering = np.argmin(reduced_costs)



    if all(a[:, entering] <= 0):

        print("Problem is unbounded.")

        break



    ratios = np.divide(plan, a[:, entering], out=np.full(n, np.inf), where=a[:, entering] > tolerance)

    leaving = np.argmin(ratios)



    pivot = a[leaving, entering]

    a[leaving] /= pivot

    plan[leaving] /= pivot

    for i in range(n):

        if i != leaving:

            factor = a[i, entering]

            a[i] -= factor * a[leaving]

            plan[i] -= factor * plan[leaving]

    basis_id[leaving] = entering



else:

    print("Maximum iterations reached. The solution may not be optimal.")



final_solution = np.zeros(m)

final_solution[basis_id] = plan

RESULT = np.dot(coefs, final_solution)

print("Final solution:")

print(final_solution)

print(f"Maximum of objective function: {RESULT:.2f}")