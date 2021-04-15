import calendar
import datetime
import time
# do NOT name file the same thing as a module
print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2019, 3))

print(calendar.monthcalendar(2019, 3))

print (calendar.calendar(2021))

day_of_the_week = calendar.weekday(2021, 4, 11)

print(day_of_the_week)

print("Hello World")

is_leap = calendar.isleap(2021)

print(is_leap)

# does not include the last year listed i.e. in this case
# it will stop counting at 2021
how_many_days = calendar.leapdays(1990, 2022)

print(how_many_days)