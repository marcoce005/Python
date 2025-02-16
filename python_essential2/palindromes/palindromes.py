def is_palindromes(s):
    return "".join(s.lower().split()) == "".join(s.lower()[::-1].split())


string = input("Insert a string to check if is palindromes:\t")

print(
    f"\nResult:\t{"It's a palindrome" if is_palindromes(string) else "It's not a palindrome"}"
)
