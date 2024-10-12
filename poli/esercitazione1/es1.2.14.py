n = 4

a = 0
b = 1

print(a, b, sep='\n')

for i in range(n - 3):
  print(a + b)
  if a > b:
    a, b = a, a + b
  else:
    a, b = a + b, b

print(a + b)
