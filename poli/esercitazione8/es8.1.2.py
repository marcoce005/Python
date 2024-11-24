def shift_left(l):
    l.append(l.pop(0))

def shift_right(l):
    l.insert(0, (l.pop(-1)))


l = [1, 7, 9, 3, 0, 4]

shift_right(l)
# shift_left(l)

print(l)