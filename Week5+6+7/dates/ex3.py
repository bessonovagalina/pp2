import datetime

today = datetime.datetime.now()

today_without_mseconds = today.replace(microsecond=0)
print(today_without_mseconds)