from operator import itemgetter


def print_mat(m):
    for r in m:
        print(*r)


def sort_colums(m):
    m.sort(key=itemgetter(0))  # ordiniamo per la colonna 0


def sort_by_len_list(m):
    # m.sort(key=lambda x: len(x), reverse=True)
    m.sort(key=len, reverse=True)


def sort_by_distance_from_centre(m):
    m.sort(key=lambda x: (x[0] ** 2) + (x[1] ** 2))


m = [[10, 20, 30, 40, 50], [7, 9, 50, 80, 60], [1, 3, 7, 9, 5]]

m2 = [[1], [1, 2], [1, 2, 3], [1, 2, 3, 5]]

m3 = [(1, 2), (4, 2), (4, 7), (9, 2), (3, 5), (3, 4), (0, 1)]

sort_colums(m)

sort_by_len_list(m2)

sort_by_distance_from_centre(m3)

print_mat(m3)
