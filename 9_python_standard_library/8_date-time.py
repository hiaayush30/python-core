from datetime import datetime
import time

print(datetime(2018,1,1))

print(datetime.now())

print(datetime.strptime("2018/01/01","%Y/%m/%d"))
dt = datetime.fromtimestamp(time.time())

print(dt)
print(f"{dt.year}/{dt.month}")
print(dt.strftime("%y/%m"))

dt2 = datetime.fromtimestamp(time.time())
print(dt2>dt)