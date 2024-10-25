"""
De Morgan:

    not (A and B) ==  anot A or not B
    
    not (A or B) ==  anot A and not B
"""

x = int(input("Inserirre numero intero:\t"))

print(f"\n\t\tnot (x > 0 and x < 100) --> {not (x > 0 and x < 100)}\nDe morgan:\tnot (x > 0) or not(x < 100) --> {not (x > 0) or not(x < 100)}")
print(f"\n\t\tnot (x > 0 or x < 100) --> {not (x > 0 or x < 100)}\nDe morgan:\tnot (x > 0) and not (x < 100) --> {not (x > 0) and not (x < 100)}")
print(f"\n\t\tnot (x > 0 or 100 < x) --> {not (x > 0 or 100 < x)}\nDe morgan:\tnot (x > 0) and not (100 < x) --> {not (x > 0) and not (100 < x)}")
print(f"\n\t\tnot (x > 0 and x < 100 or x == -1) --> {not (x > 0 and x < 100 or x == -1)}\nDe morgan:\tnot (x > 0 and x < 100) and not (x == -1) --> {not (x > 0 and x < 100) and not (x == -1)}")
