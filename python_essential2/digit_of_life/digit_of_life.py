import re


def sum_date(d):
    if len(d) == 1:
        return d

    return sum_date(str(sum([int(n) for n in list(d)])))


REGEX = r"^(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])\d{4}$"

date = input("Digit the date using this format [DDMMYYYY]:\t")

if not re.match(REGEX, date):
    print("Invalid date.")
else:
    print(f"\nThe digit of your life is:\t{sum_date(date)}")
