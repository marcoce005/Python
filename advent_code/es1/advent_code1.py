def cal_distance(l1, l2):
    l1.sort()
    l2.sort()
    tot = 0

    [tot := tot + abs(l1[i] - l2[i]) for i in range(len(l1))]

    return tot


def create_lists(path):
    l = [[], []]
    with open(path) as file:
        for line in file:
            line = line.rstrip().split()
            l[0].append(int(line[0]))
            l[1].append(int(line[1]))
    return l[0], l[1]


l1, l2 = create_lists("./numeri_casuali.txt")

print(f"Distanza delle liste:\t{cal_distance(l1, l2)}")
