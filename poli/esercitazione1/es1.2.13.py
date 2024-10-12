n = 4

a = 0
b = 1

for i in range(n - 3):
  if a > b:
    a, b = a, a + b
  else:
    a, b = a + b, b

print(a + b)
