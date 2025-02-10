def crypt(s):
    return "".join([chr(ord(c) + 1) if c.isalpha() else c for c in s])


def decrypt(s):
    return "".join([chr(ord(c) - 1) if c.isalpha() else c for c in s])


mod = bool(int(input("[0] --> to crypt\n[1] --> to decrypt\n...")))
string = input(f"Text to {"de" if mod else ''}crypt:\t")

print(f"Output:\n{decrypt(string) if mod else crypt(string)}")
