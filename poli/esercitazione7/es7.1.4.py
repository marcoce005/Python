def is_local_max(a, b, c):
    return b > a and b > c


def find_local_max(l):
    return [
        (i, l[i])
        for i in range(1, len(l) - 1)
        if is_local_max(l[i - 1], l[i], l[i + 1])
    ]


def min_distance(l):
    min_dist_index = l[1][0] - l[0][0]

    list_min = [
        [l[i], l[i + 1]]
        for i in range(0, len(l) - 1)
        if l[i + 1][0] - l[i][0] <= min_dist_index
    ]

    return [
        e
        for e in list_min
        if e[1][0] - e[0][0] == list_min[-1][1][0] - list_min[-1][0][0]
    ]


s = input("Inserire i numeri [interi] separati da uno spazio:\t")

l = [int(e) for e in s.split()]

local_max = find_local_max(l)

if len(local_max) == 0:
    print("Non ci sono massimi locali")
else:
    print("\nIndice\t\tValore")
    [print(f"{e[0]}\t\t{e[1]}") for e in local_max]

    nearest_couple = min_distance(local_max) if len(local_max) >= 2 else None

    (
        (
            print("\nCoppie più vicine:\n"),
            [
                print(f"{e[0]} - {e[1]}\tdistanza: {e[1][0] - e[0][0]}")
                for e in nearest_couple
            ],
        )
        if nearest_couple != None
        else None
    )
