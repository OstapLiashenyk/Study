import numpy as np

M = 1000
n, m = 2, 5
a = np.array([
    [-1, 4, -1, 1, 0],
    [4, -1, -1, 0, 1]
], dtype=float)
plan = np.array([-8, -2], dtype=float)
coefs = np.array([4, 4, 6, 0, 0], dtype=float)
basis_id = np.array([3, 4], dtype=int) - 1
RESULT = 0

while True:
    RESULT = sum(coefs[basis_id[i]] * plan[i] for i in range(n))
    print("Basis\tC(bas)\tPlan\t", end="")
    for i in range(m):
        print(f"y{i+1}\t", end="")
    print("\n")

    for i in range(n):
        print(f"y{basis_id[i]+1}\t{coefs[basis_id[i]]}\t{plan[i]}\t", end="")
        for j in range(m):
            print(f"{a[i, j]}\t", end="")
        print()
    print()

    print("RESULT:", RESULT)
    print("-" * 60)

    change_id = np.argmin(plan)
    if plan[change_id] >= 0:
        break

    delta = np.full(m, M)
    for i in range(m):
        if a[change_id, i] < 0:
            delta[i] = abs(coefs[i] / a[change_id, i])

    min_id = np.argmin(delta)
    min_num = delta[min_id]

    basis_id[change_id] = min_id
    test_num = a[change_id, min_id]

    a[change_id] /= test_num
    plan[change_id] /= test_num

    for g in range(n):
        if g == change_id or a[g, min_id] == 0:
            continue
        divider = a[g, min_id]
        a[g] -= a[change_id] * divider
        plan[g] -= plan[change_id] * divider


print("Final solution:")
for i, val in enumerate(plan):
    print(f"y{basis_id[i]+1}: {val}")
print(f"Maximum of objective function: {RESULT}")
