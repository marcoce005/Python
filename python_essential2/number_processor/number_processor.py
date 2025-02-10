line = input("Enter a line of numbers - separate them with spaces: ").split()

try:
    if len(line) == 0:
        raise(FileExistsError)
    
    tot = 0
    [tot := tot + float(e) for e in line]
    
    print(f"\nTotal:\t{tot}")
except FileExistsError:
    print("\nYou don't insert anything")
except Exception:
    print(*line, sep=" ")
    print("\nIs not a number or a sequence of numerbs")
    