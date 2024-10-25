a = int(input("n1 = "))
b = int(input("n2 = "))
c = int(input("n3 = "))

print(f"{a} > {b} > {c}\tdecreasing") if a > b > c else (print(f"{a} > {b} > {c}\tincreasing") if a < b < c else print("neither"))
