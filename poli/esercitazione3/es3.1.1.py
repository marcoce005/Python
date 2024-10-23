from math import sqrt

r = 1 == 1
r1 = 1 == 1.0
r2 = 2.0 == sqrt(4)
r3 = '1' == 1
r4 = 'ciao' == 'Ciao'


print(f"1 == 1 --> {r}", f"1 == 1.0 --> {r1}", f"2.0 == sqrt(2) --> {r2}", f"'1' == 1 --> {r3}", f"'ciao' == 'Ciao' --> {r4}", sep='\n')
