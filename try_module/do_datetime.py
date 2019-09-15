"""
    Created by Xiaozhong.
    Copyright (c) 2019/9/6 Xiaozhong. All rights reserved.
"""
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015, 5, 22, 12, 20)
print(dt)

print(dt.timestamp())
t = 1429417200.0
print(datetime.fromtimestamp(t))
cday = datetime.strptime('2015/6-1 18:20:20', '%Y/%m-%d %H:%M:%S')
print(cday)
