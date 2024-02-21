import datetime

today=datetime.datetime.now()
day=today-datetime.timedelta(days=5)
print(day)