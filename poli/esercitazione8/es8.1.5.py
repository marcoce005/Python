def merge(a, b):
    merged = []
    for i in range(len(a) if len(a) > len(b) else len(b)):
        if i < len(a):
            merged.append(a[i])
        if i < len(b):
            merged.append(b[i])

    return merged


a = [1, 4, 9, 16]
b = [9, 7, 4, 9, 11]

print(f"Merged list:\t{merge(a, b)}")
