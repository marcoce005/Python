def find_bigger_than_double_avg(l, avg):
    return [e for e in l if e > avg * 2]


def cal_media(l):
    return sum(l) / len(l)


def main():
    n = input("Inserire un numero:\t")
    l = []

    while n != "" or len(l) < 2:
        if n == "" and len(l) < 2:
            print("Inserire minimo 2 numeri")
        elif not n.replace(".", "").isdigit():
            print("Inserire SOLO numeri")
        else:
            n = float(n)
            l.append(n)

        n = input("Inserire un numero:\t")

    avg = cal_media(l)
    bigger = find_bigger_than_double_avg(l, avg)

    print("\nMedia:\t", avg)

    if len(bigger) != 0:
        print("\nNumeri che superano il doppio della media:\t", *bigger)
    else:
        print("\nNon ci sono numeri che superano il doppio della media")


main()
