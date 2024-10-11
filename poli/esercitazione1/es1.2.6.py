c = 1000

print(*[c := c * 1.05 for i in range(0, 3)], '', sep=' €\n')
