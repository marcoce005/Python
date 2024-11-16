def special_sum(l, string=False):
    return (
        "".join([e + (" - " if i % 2 == 0 else " + ") for i, e in enumerate(l)])[:-3]
        if string
        else sum([int(e) if i % 2 == 0 else -int(e) for i, e in enumerate(l)])
    )


s = input("Inserire tutti i numeri [interi] separati da uno spazio:\t")
l = s.split()

print(f"{special_sum(l, string = True)} = {special_sum(l)}")
