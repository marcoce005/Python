file = open("./worldpop.txt", "r")

for i, line in enumerate(file):
    if i == 0 or int(line.rsplit(" ", 1)[1]) > max_pop:
        max_state, max_pop = line.rsplit(" ", 1)[0], int(line.rsplit(" ", 1)[1])
        
    if i == 0 or int(line.rsplit(" ", 1)[1]) < min_pop:
        min_state, min_pop = line.rsplit(" ", 1)[0], int(line.rsplit(" ", 1)[1])


print(f"Popolazione massima:\t{max_pop} in {max_state}")

print(f"Popolazione minima:\t{min_pop} in {min_state}")
