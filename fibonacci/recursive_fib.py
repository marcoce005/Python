import sys


def fib(n = 10):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(int(sys.argv[1])))
