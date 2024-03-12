import numpy as np
from prettytable import PrettyTable


def fill_f_(f_, matrix):
    for i in range(len(f_)):
        f_[i][0] = np.amax(matrix[i])
        index = np.where(matrix[i] == np.amax(matrix[i]))
        f_[i][1] = index[0][0]


def find_d(table, iter, k):
    lst_ = [0]
    for i in table[iter - 1]:
        if i[0] == k:
            lst_.append(i[1])
    return max(lst_)


def solve(table, invest):
    iter = len(table)

    inv = invest
    matrix = np.array([[0] * (invest + 1) for i in range(invest + 1)], dtype=float)

    f_ = np.array([[[0, 0] for i in range(invest + 1)] for j in range(iter + 1)], dtype=float)
    way = []

    while iter > 0:
        for x in range(invest + 1):
            for k in range(invest + 1):
                if k <= x:
                    matrix[x][k] = find_d(table, iter, k) + f_[iter][x - k][0]
        fill_f_(f_[iter - 1], matrix)
        iter -= 1

    f_ = np.delete(f_, -1, axis=0)

    for i in range(len(f_)):
        t = f_[i][inv][1]
        way.append((i + 1, t))
        inv -= int(t)

    return way, np.amax(matrix[-1])


invest = 3
table = [[[2, 0.5], [4, 0.8], [2, 5.7], [4, 1.2], [5, 1.3]],
         [[3, 0.8], [2, 0.4], [4, 1.4], [3, 0.9], [5, 1.3]],
         [[2, 0.5], [3, 0.6], [4, 1.4], [4, 1.2], [3, 0.8]]]

write = PrettyTable()
write.field_names = ["1 company", "2 company", "3 company"]

way, incomes = solve(table, invest)

row_data = []
for i, j in way:
    row_data.append(j)
write.add_row(row_data)

print(write)
print(f"Your incomes are {incomes}")

