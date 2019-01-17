#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'derek'

from datetime import datetime

# 获取当前时间
now = datetime.now()
print(now)
print(type(now))

# 获取指定时间
dt = datetime(2018, 11, 30, 16, 32)
print(dt)
# 时间戳的使用
print(dt.timestamp())
# timestamp也可以直接被转换到UTC标准时区的时间
t = 1543566720.0
print(datetime.fromtimestamp(t))  # 本地时间
print(datetime.utcfromtimestamp(t))  # UTC时间

# 格式化日期 strptime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# 时间转字符串 str
print(now.strftime('%a, %b %d %H:%M'))

# 时间加减
from datetime import datetime, timedelta

print('-------------')
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=2, hours=12))

from datetime import timezone

# tzinfo 设置时区
# 创建时区
tz_utc_8 = timezone(timedelta(hours=8))
# 强制设置时区
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00

# 时区转换
# utcnow
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# 2015-05-18 09:05:12.377316+00:00
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# 2015-05-18 17:05:12.377316+08:00
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# 2015-05-18 18:05:12.377316+09:00
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
# 2015-05-18 18:05:12.377316+09:00

import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    tz = re.match(r'UTC([+-]\d+):\d+', tz_str).group(1)
    tz_utc = timezone(timedelta(hours=int(tz)))
    t=datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    t=t.replace(tzinfo=tz_utc)
    return t.timestamp()



# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')