from datetime import datetime

d = datetime(2020, 11, 4, 14, 53, 0)
print(d.strftime("%Y/%m/%d %H:%M:%S"))
print(d.strftime("%y/%B/%d %H:%M:%S %p"))
print(d.strftime("%a, %Y %b %d"))
print(d.strftime("%A, %Y %B %d"))
print(d.strftime("Weekday: %w"))
print(d.strftime("Day of the year: %j"))
print(d.strftime("Week number of the year: %W"))