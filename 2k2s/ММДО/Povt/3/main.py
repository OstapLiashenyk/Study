import numpy as np

n, m = 3, 5

a = np.array([
    [5, -2, 1, 0, 0],
    [-1, 1, 0, 1, 0],
    [1, 1, 0, 0, 1]
], dtype=float)


plan = np.array([7, 5, 6], dtype=float)


coefs = np.array([1, 1, 0, 0, 0], dtype=float)


basis_id = np.array([2, 3, 4], dtype=int)

max_iterations = 100
tolerance = 1e-5

for iteration_counter in range(max_iterations):
    print(f"Iteration {iteration_counter + 1}")


    tmp_vector = np.dot(coefs[basis_id], a) - coefs

    RESULT = np.dot(coefs[basis_id], plan)

    if np.all(tmp_vector >= -tolerance):
        print("Optimal solution found.")
        break


    entering = np.argmin(tmp_vector)
    if tmp_vector[entering] >= -tolerance:
        print("Solution is optimal.")
        break


    ratios = np.divide(plan, a[:, entering], out=np.full(n, np.inf), where=a[:, entering] > tolerance)
    leaving = np.argmin(ratios)
    if a[leaving, entering] <= tolerance:
        print("Problem is unbounded.")
        break


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
print("Final solution:")
print(final_solution)
print(f"Maximum of objective function: {RESULT:.2f}")
