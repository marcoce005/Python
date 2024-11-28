def print_mat(m):
    for r in m:
        print(*r)


def exist_index(m, r, c):
    return r >= 0 and r < len(m) and c >= 0 and c < len(m[0])


def neighbor_average(values, row, column):
    tot = 0
    n = 0

    for r, c in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if exist_index(values, row + r, column + c):
            tot += values[row + r][column + c]
            n += 1
    return tot / n


values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print_mat(values)

print(f"\n\nMedia dei vicini di (1, 1):\t{neighbor_average(values, 1, 1)}")
