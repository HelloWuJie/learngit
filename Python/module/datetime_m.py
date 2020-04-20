from datetime import datetime
#获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))
#获取指定日期和时间
dt = datetime(2010,3,20,12,12,59)
print(dt)

#datetime转换为timestamp
timestamp = dt.timestamp()
print(timestamp)

#timestamp转换为UTC本地时间（北京时间）
date_time = datetime.fromtimestamp(timestamp)
print(date_time)
#timestamp转换为UTC标准时区的时间（格林威治标准时间）
date_time = datetime.utcfromtimestamp(timestamp)
print(date_time)

#str转换为datetime

cday = datetime.strptime('2015-6-1 18:23:12','%Y-%m-%d %H:%M:%S')
print(cday)