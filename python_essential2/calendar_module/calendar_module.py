from calendar import Calendar


class MyCalendar(Calendar):
    def __init__(self, firstweekday=0):
        super().__init__(firstweekday)

    def __filter_only_correct_days(self, l, n):  # remove days of the others months
        return len([el for e in l for el in e if el[0] != 0 and el[1] == n])

    def count_weekday_in_year(self, year, weekday):
        return sum(
            [
                self.__filter_only_correct_days(
                    Calendar.monthdays2calendar(self, year, i + 1), weekday
                )
                for i in range(12)
            ]
        )


cal = MyCalendar()
print(f"year=2019, weekday=0:\t{cal.count_weekday_in_year(year=2019, weekday=0)}")
print(f"year=2000, weekday=6:\t{cal.count_weekday_in_year(year=2000, weekday=6)}")
