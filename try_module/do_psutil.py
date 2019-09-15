"""
    Created by Xiaozhong.
    Copyright (c) 2019/9/6 Xiaozhong. All rights reserved.
"""
import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())


# for x in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))


print(psutil.virtual_memory())


print(psutil.disk_partitions())
print(psutil.disk_usage('A:\\'))
print(psutil.disk_io_counters())


print('\n')
print(psutil.net_io_counters())
print(psutil.net_if_addrs())
print(psutil.net_connections())

try:
    p = psutil.Process(13260)
    print(p.name())
    print(p.exe())
    print(p.terminate())
except Exception as e:
    pass

psutil.test()