def merge_sorted(a, b):
    merged = a + b

    for i in range(len(merged)):
        minimum = min(merged[: len(merged) - i])
        merged.append(minimum)
        merged.remove(minimum)

    return merged


a = [1, 4, 9, 16]
b = [4, 7, 9, 9, 11]

print(f"Merged and sorted list:\t{merge_sorted(a, b)}")
