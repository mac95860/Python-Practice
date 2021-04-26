import datetime

today = datetime.date.today()
print(today)

birthday = datetime.date(1990, 5, 21)
print(birthday)

days_since_birth = (today - birthday).days
print(days_since_birth)

tdelta = datetime.timedelta(days=10)
print(today + tdelta)