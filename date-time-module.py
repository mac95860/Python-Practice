import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(1990, 5, 21)
print(birthday)

days_since_birth = (today - birthday).days
print(days_since_birth)

tdelta = datetime.timedelta(days=10)
print(today - tdelta)

print(today.month)
# Monday is beginning of the week and has value of 0
print(today.weekday())

# hour, minute, second, milisecond

print(datetime.time(7, 2, 20, 15))
# datetime.date (Y, M, D)
# datetime.time (H, M, S, MS)
# datetime.datetime (Y, M, D, h , m , s, ms)

# add 10 hours to current day
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

datetime_today = datetime.datetime.now(tz = pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)

for tz in pytz.all_timezones:
    print(tz)

