def filter(l, start, end):
    # return [e for e in l if e > 5]
    i = 0
    while i < len(l):
        if l[i] < start or l[i] > end:
            l.pop(i)
        else:
            i += 1

def print_list(l):
    for i, e in enumerate(l):
        if i == len(l) - 1:
            print(e)
        else:
            print(e, end=", ")

def main():
    n = input("Inserire un numero [intero] o [N] per terminare:\t")
    l = []
    
    while n != "N":
        if n.isdigit():
            n = int(n)
            l.append(n)
        else:
            print("Non hai inserito un numero riprova")
        n = input("Inserire un numero [intero] o [N] per terminare:\t")
        
    if len(l) > 2:
        filter(l, 10, 100)
        l.sort(reverse=True)
        print("\n\nI numeri inseriti sono:\t", end="")
        print_list(l)
        

main()
