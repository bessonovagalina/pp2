import datetime

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
dif = today - yesterday
print(dif.total_seconds())
