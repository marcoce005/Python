from random import randint


def print_map(m):
    for r in m:
        for e in r:
            print(f"{e:>5}", end="")
        print()


def flood_map(heights, water_level):
    return [["*" if e < water_level else " " for e in r] for r in heights]


def range_steps():
    return


N = 10
WATER_LEVEL = 69

heights = [[randint(0, 100) for _ in range(N)] for _ in range(N)]

print_map(heights)

i = WATER_LEVEL / 10
for _ in range(10):
    print(f"\n\nWater level:\t{i}")
    print_map(flood_map(heights, i))
    i += WATER_LEVEL / 10
