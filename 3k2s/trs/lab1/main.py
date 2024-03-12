import numpy as np
import math
import threading
import time
import matplotlib.pyplot as plt

# Функція для обчислення значення елемента матриці
def calculate_matrix_value(i, j):
    return math.sin(i + j)

# Функція для обчислення значення елемента вектора
def calculate_vector_value(i):
    return math.cos(i)

# Функція для заповнення матриці та вектора даними
def fill_data(matrix_size):
    n = matrix_size
    matrix = np.zeros((n, n))
    vector = np.zeros(n)
    for i in range(n):
        for j in range(n):
            matrix[i, j] = calculate_matrix_value(i, j)
        vector[i] = calculate_vector_value(i)
    return matrix, vector

# Функція для секвенційного множення матриці на вектор
def multiply_sequential(matrix, vector):
    return np.dot(matrix, vector)

# Робоча функція для паралельного множення, обчислює частину результату
def worker_multiply_threads(matrix, vector, result, start, end):
    """Функція для обчислення частини результату множення матриці на вектор використовуючи потоки"""
    for i in range(start, end):
        result[i] = np.dot(matrix[i], vector)

def multiply_parallel_threads(matrix, vector, num_threads):
    """Функція для паралельного множення використовуючи потоки"""
    n = len(matrix)
    result = np.zeros(n)
    threads = []
    chunk_size = n // num_threads
    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else n
        t = threading.Thread(target=worker_multiply_threads, args=(matrix, vector, result, start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return result

if __name__ == "__main__":
    n = 90
    matrix, vector = fill_data(n)

    # Секвенційне множення для порівняння
    start_seq = time.perf_counter()
    result_seq = multiply_sequential(matrix, vector)
    end_seq = time.perf_counter()
    seq_time = end_seq - start_seq
    print(f"Sequential time: {seq_time:.6f} s")

    # Паралельне множення
    num_threads = [1, 2, 4, 8]
    parallel_times = []
    efficiencies = []
    for thread in num_threads:
        start_par = time.perf_counter()
        result_par = multiply_parallel_threads(matrix, vector, thread)
        end_par = time.perf_counter()
        par_time = end_par - start_par
        parallel_times.append(par_time)

        speedup = seq_time / par_time
        efficiency = (speedup / thread) * 100
        efficiencies.append(efficiency)

        print(f"threads - {thread}")
        print(f"Parallel time: {par_time:.6f} s")
        print(f"Parallel Speedup: {speedup:.2f}, Parallel Efficiency: {efficiency:.2f}%")



    # Створюємо графіки
    plt.figure(figsize=(10, 5))

    # Графік часу виконання
    plt.subplot(1, 2, 1)
    plt.plot(num_threads, parallel_times, marker='o', linestyle='-', color='b')
    plt.plot(num_threads, [seq_time] * len(num_threads), linestyle='--', color='r', label='Sequential')
    plt.title('Parallel Execution Time')
    plt.xlabel('Number of Threads')
    plt.ylabel('Time (seconds)')
    plt.legend()

    # Графік ефективності
    plt.subplot(1, 2, 2)
    plt.plot(num_threads, efficiencies, marker='o', linestyle='-', color='g')
    plt.title('Parallel Efficiency')
    plt.xlabel('Number of Threads')
    plt.ylabel('Efficiency (%)')

    plt.tight_layout()
    plt.show()