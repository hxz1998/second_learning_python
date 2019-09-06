# -*- coding: utf-8 -*-
"""
 Created by Monkey at 2019/9/5
"""
from multiprocessing import Pool

import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(9)
    for i in range(9):
        p.apply_async(long_time_task, args=(i, ))
    print('等待所有子进程运行完毕')
    p.close()
    p.join()
    print('done')
