"""
    year is leap if:
        year is grater than 1582 (Giulian's calendar),
        last 2 digit of the year are divisible by 4,
        the year is divisible by 400 or it can't be divisible by 100
"""

"""
def is_leap(year):
    return (
        year > 1582
        and int(str(year)[2:]) % 4 == 0
        and (year % 100 != 0 or year % 400 == 0)
    )
"""

yyyy = int(input("inserire l'anno:\t"))

# print(f"{yyyy} --> {is_leap(yyyy)}")

print(f"{yyyy} --> {yyyy > 1582 and int(str(yyyy)[2:]) % 4 == 0 and (yyyy % 100 != 0 or yyyy % 400 == 0)}")
