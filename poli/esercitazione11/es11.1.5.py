def sparse_array_2_list(d):
    return [d[i] if i in d.keys() else 0 for i in range(max(d.keys()) + 1)]


def sparse_array_sum(a, b):
    c = {}

    for k, v in a.items():
        c[k] = c[k] + v if k in c.keys() else v

    for k, v in b.items():
        c[k] = c[k] + v if k in c.keys() else v

    return c


a = {5: 4, 9: 2, 10: 9}
b = {4: 2, 6: 4, 2: 7, 11: 2, 5: 1, 9: -1, 10: 60}

print(f"Somma array spari:\n{sparse_array_sum(a, b)}")

print("\nArray:\n")

print(f"a = {sparse_array_2_list(a)}")
print(f"b = {sparse_array_2_list(b)}")
