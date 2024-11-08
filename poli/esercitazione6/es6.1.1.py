def count_vowels(s):
    return len([c for c in s.lower() if c in "aeiou"])

print(f"C'era una volta tanto tempo fa...\nVocali:\t{count_vowels("C'era una volta tanto tempo fa...")}")
