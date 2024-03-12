import math
from scipy.optimize import minimize_scalar

def f(x):
    return 10 * x * math.log(x) - (x ** 2) / 2

def fibonacci_search(a, b, eps):
    fib = [1, 1]
    while (b - a) / fib[-1] > eps:
        fib.append(fib[-1] + fib[-2])

    n = len(fib) - 1
    k = 0
    x1 = a + (fib[n - k - 3] / fib[n - k - 1]) * (b - a)
    x2 = a + (fib[n - k - 2] / fib[n - k - 1]) * (b - a)

    iteration = 1
    while abs(b - a) > eps:
        print(f"Iteration {iteration}: [{a}] - {x1} - {x2} - [{b}]")

        if f(x1) > f(x2):
            a = x1
            x1 = x2
            x2 = a + (fib[n - k - 2] / fib[n - k - 1]) * (b - a)
        else:
            b = x2
            x2 = x1
            x1 = a + (fib[n - k - 3] / fib[n - k - 1]) * (b - a)

        if k < n - 3:
            k += 1
        else:
            break

        iteration += 1
    return (a + b) / 2

a, b = 0.5, 1
eps = 0.05

result = fibonacci_search(a, b, eps)
print(f"\nResult= {f(result)}\nX: {result}")
print("-----------------------------------------------")
res = minimize_scalar(f, bounds=(0.5, 1), method='bounded', options={'xatol': 0.05})
print("Result by scipy: ", res.fun)
print("X by scipy: ", res.x)