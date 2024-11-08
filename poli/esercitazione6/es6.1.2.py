def count_words(s):
    w = 0
    same_word = False
    for c in s:
        if c != " " and not same_word:
            w += 1
            same_word = True
        elif c == " ":
            same_word = False
    return w


# print(f"Mary had a little lamb\nParole:\t{count_words("Mary had a little lamb")}")

print(count_words("  Ciro    è    stato    qui  "))
