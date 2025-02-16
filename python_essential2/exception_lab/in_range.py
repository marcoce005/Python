def read_int(prompt, min, max):
    try:
        n = int(input(prompt))
        assert -10 < n < 10
        return n
    except ValueError:
        print("Error: wrong input")
    except AssertionError:
        print("Error: the value is not within permitted range (min..max)")
    return read_int(prompt, min, max)


v = read_int("Enter a number from -10 to 10:\t", -10, 10)

print("The number is:", v)
