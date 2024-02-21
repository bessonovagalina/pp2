import datetime

today=datetime.datetime.now()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)
print(f"yesterday :  {yesterday}")
print(f"today : {today}")
print(f"tomorrow : {tomorrow}")