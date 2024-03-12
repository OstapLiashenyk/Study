import random
import threading

def fill_matrix(matrix, size):
    """Fills a matrix with random integers between -10 and 10."""
    for i in range(size):
        for j in range(size):
            matrix[i][j] = random.randint(-10, 10)

def print_matrix(matrix, size):
    """Prints the matrix."""
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=" ")
        print()

def find_max_elements(matrix, result, row, schedule_type, chunk_size):
    """Calculates the sum of positive elements in a given row of the matrix."""
    sum_positive = max(item for item in matrix[row])
    result[row] = sum_positive
    thread_id = threading.get_ident()
    print(f"Потік {thread_id} обробив рядок {row} з розподілом {schedule_type}, чанк = {chunk_size}")

if __name__ == "__main__":
    size = int(input("Введіть розмір матриці (n x n): "))
    matrix_a = [[0] * size for _ in range(size)]
    matrix_b = [[0] * size for _ in range(size)]
    sum_a = [0] * size
    sum_b = [0] * size

    # Filling matrices A and B with random values
    fill_matrix(matrix_a, size)
    fill_matrix(matrix_b, size)

    # Printing matrices A and B
    print("Матриця A:")
    print_matrix(matrix_a, size)
    print("\nМатриця B:")
    print_matrix(matrix_b, size)

    # Processing matrix A in threads
    threads = []
    for i in range(size):
        thread = threading.Thread(target=find_max_elements, args=(matrix_a, sum_a, i, "dynamic", 6))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    threads.clear()
    # Processing matrix B in threads
    for i in range(size):
        thread = threading.Thread(target=find_max_elements, args=(matrix_b, sum_b, i, "guided", 6))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

    # Printing the sums of positive elements in matrices A and B
    print("\nСума позитивних елементів у рядках матриці A:")
    for sum_pos in sum_a:
        print(sum_pos, end=" ")

    print("\n\nСума позитивних елементів у рядках матриці B:")
    for sum_pos in sum_b:
        print(sum_pos, end=" ")
    print()
