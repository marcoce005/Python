def find_word(s1, s2):
    l = []
    [
        l.append(c)
        for i, c in enumerate(s2.lower())
        if c in s1 and (len(l) == 0 or c != l[-1])
    ]
    return s1 in "".join(l)


word = input("Digit the word to search:\t")
second = input("Digit the word where search:\t")

print(f"\nThere is the word?\n{'Yes' if find_word(word, second) else 'No'}")
