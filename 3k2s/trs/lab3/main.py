import concurrent.futures
import sympy as sp
import time
import threading
import os

lock = threading.Lock()
file_name = "integration_results.txt"


def left_rectangle_approximation(expression, variable, lower_bound, upper_bound, num_rectangles):
    delta_x = (upper_bound - lower_bound) / num_rectangles
    x_values = [lower_bound + i * delta_x for i in range(num_rectangles)]
    total_area = sum(expression.subs(variable, x_val) for x_val in x_values) * delta_x
    return total_area


def integrate_function(expression, variable, bounds, step_size):
    num_rectangles = 100
    result = left_rectangle_approximation(expression, variable, bounds[0], bounds[1], num_rectangles)
    return result


def thread_function(name, expression, variable, bounds, step_size):
    result = integrate_function(expression, variable, bounds, step_size)
    return result


x1 = sp.symbols('x')
expression1 = 1 / (x1 * (x1 ** 2 + 3.5 ** 2))
brakes_integral1 = [4, 6]

x2 = sp.symbols('x')
expression2 = 1 / (1 + sp.cos(0.8 * x2) + sp.sin(0.8 * x2))
brakes_integral2 = [0.6, 1.6]

integrals = [
    (expression1, x1, brakes_integral1, 0.00002),
    (expression2, x2, brakes_integral2, 0.00002)
]

if os.path.exists(file_name):
    os.remove(file_name)

steps = [0.001, 0.0001, 0.00001, 0.00002]
num_cores = [1, 2, 4, 8]
results = []
time_measurements = {}

for step_size in steps:
    for cores in num_cores:
        start_time = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=cores) as executor:
            futures = [executor.submit(thread_function, f"Thread-{i}", expr, var, bounds, step_size)
                       for i, (expr, var, bounds, _) in enumerate(integrals)]
            concurrent.futures.wait(futures)
        end_time = time.time()

        execution_time = end_time - start_time
        time_measurements[(step_size, cores)] = execution_time

        if cores == 1:
            base_time = execution_time

        speedup = base_time / execution_time if cores != 1 else 1
        print(f"Step size: {step_size}, Cores: {cores}, Time taken: {execution_time}, Speedup: {speedup}")

with open(file_name, "a") as f:
    for (step_size, cores), execution_time in time_measurements.items():
        speedup = base_time / execution_time if cores != 1 else 1
        f.write(f"Step size: {step_size}, Cores: {cores}, Time taken: {execution_time}, Speedup: {speedup}\n")
