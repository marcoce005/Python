def are_anagrams(s1, s2):
    return sorted([c for c in list(s1.lower())]) == sorted(
        [c for c in list(s2.lower())]
    )


string1 = input("Insert first string:\t")
string2 = input("Insert second string:\t")

print(f"\nResult:\t{'Anagrams' if are_anagrams(string1, string2) else 'Not anagrams'}")
