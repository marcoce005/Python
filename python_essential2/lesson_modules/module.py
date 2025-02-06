#!/usr/bin/env python3 


__counter = 0       # use __ or _ to named variable's module it's a convetion

def suml(the_list):
    global __counter
    __counter += 1
    
    return sum(the_list)


def prodl(the_list):
    global __counter
    __counter += 1
    prod = 1
    
    [prod := prod * e for e in the_list]
    return prod


if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you.")
    
    my_list = [i + 1 for i in range(5)]

    print(suml(my_list) == 15)
    print(prodl(my_list) == 120)
