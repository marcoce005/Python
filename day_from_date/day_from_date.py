import sys, re


def is_leap(year):
    """
    year is leap if:
        year is grater than 1582 (Giulian's calendar),
        last 2 digit of the year are divisible by 4,
        the year is divisible by 400 or it can be divisible by 100
    """
    return (
        year > 1582
        and int(str(year)[2:]) % 4 == 0
        and (year % 100 != 0 or year % 400 == 0)
    )


def day_in_month(month, year):
    return (
        30
        if month in [4, 6, 9, 11]
        else ((29 if is_leap(year) else 28) if month == 2 else 31)
    )


def day_number(day, month, year):
    tot = 0
    [tot := tot + day_in_month(i, year) for i in range(1, month)]
    return day + tot


def get_first_of_the_year(year):
    """
    y = last 2 digit of the year
    d = (y mod 28) + [ ((y mod 28) - 1) / 4] mod 7
    also...
    d = { [(y mod 28) * 5 / 4] - 1 / 4 } mod 7
    """
    return int((((int(str(year)[2:]) % 28) * 5 / 4) - 0.25) % 7)


def get_centenario(year):
    """
    first 2 digit of year mod 4
    4k   (1600-2000-2400-...) Saturday   6
    4k+1 (1700-2100-2500-...) Friday     4
    4k+2 (1800-2200-2600-...) Wensday    2
    4k+3 (1900-2300-2700-...) Monday     0
    """
    dic_cent = [6, 4, 2, 0]
    return dic_cent[int(str(year)[:2]) % 4]


days = ["Monday", "Tuesday", "Wendsdey", "Thursday", "Friday", "Saturday", "Sunday"]


regex_date = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})$"

date = sys.argv[1]

if re.match(regex_date, date):
    dd = int(date[:2])
    mm = int(date[3:5])
    yyyy = int(date[6:])

    n_day = day_number(dd, mm, yyyy)
    n_cent = get_centenario(yyyy)
    n_first_of_year = get_first_of_the_year(yyyy)
    
    index = ((n_cent + n_day + n_first_of_year) % 7) -1
    
    print("{}\t{}".format(days[index], date))
else:
    print("Your date {} don't respect the format dd/mm/yyyy".format(date))
