from random import randint


def find_sequence(l):
    hits = [0] * 6
    pre = l[0]
    tmp = 0

    for i in range(1, len(l)):
        if l[i] == pre:
            tmp += 1
        else:
            if tmp > hits[pre - 1]:
                hits[pre - 1] = tmp
            tmp = 0
        pre = l[i]
    return max(hits) + 1, hits.index(max(hits)) + 1


def print_with_max(times, number, l):
    start = "".join([str(e) for e in l]).index(str(number) * times)
    end = start + times - 1

    for i in range(len(l)):
        if i == start:
            print(f"({l[i]} ", end="")
        elif i == end:
            print(f"{l[i]}) ", end="")
        else:
            print(f"{l[i]} ", end="")


l = [randint(1, 6) for _ in range(20)]

print(l)

print_with_max(*find_sequence(l), l)
