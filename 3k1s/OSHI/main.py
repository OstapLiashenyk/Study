import math


def find_centroid(points):
    n = len(points)

    # Ініціалізуємо початкові координати центроїду
    centroid_x = sum(point[1] for point in points) / n
    centroid_y = sum(point[0] for point in points) / n

    # Початкова сума відстаней
    min_distance_sum = sum(math.hypot(point[1] - centroid_x, point[0] - centroid_y) for point in points)

    # Ітеративно покращуємо координати центроїду
    delta = 1e-7  # Точність обчислень
    while True:
        new_x = sum(point[1] / math.hypot(point[1] - centroid_x, point[0] - centroid_y) for point in points)
        new_y = sum(point[0] / math.hypot(point[1] - centroid_x, point[0] - centroid_y) for point in points)

        if abs(new_x - centroid_x) < delta and abs(new_y - centroid_y) < delta:
            break

        centroid_x, centroid_y = new_x, new_y
        min_distance_sum = sum(math.hypot(point[1] - centroid_x, point[0] - centroid_y) for point in points)

    return round(min_distance_sum, 7)


# Введення кількості точок
n = int(input())
points = []

# Зчитування координат точок
for _ in range(n):
    y, x = map(int, input().split())
    points.append((y, x))

# Знаходження центроїда та виведення результату з точністю до 7 знаків після коми
result = find_centroid(points)
print(result)
