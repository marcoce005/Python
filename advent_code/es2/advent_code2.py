def get_data(path):
    with open(path) as file:
        return [[int(e) for e in line.split()] for line in file]


def print_mat(m):
    for r in m:
        print(*r)


def check_sort(l):
    return sorted(l) == l or sorted(l, reverse=True) == l


def check_delta(l):
    for i in range(len(l) - 1):
        if abs(l[i] - l[i + 1]) > 3 or abs(l[i] - l[i + 1]) < 1:
            return False
    return True


def check_reports(r):
    return [check_sort(levels) and check_delta(levels) for levels in r]


reports = get_data("./input.txt")

print_mat(reports)

reports_checked = check_reports(reports)

print(f"\n\nThere are {reports_checked.count(True)} safe reports")

print("\nSafe reports are:\n")
print(*[reports[index] for index in [i for i, e in enumerate(reports_checked) if e]], sep="\n")
