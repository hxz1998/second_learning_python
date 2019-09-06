# -*- coding: utf-8 -*-
"""
 Created by Monkey at 2019/9/5
"""
from multiprocessing import Process
import os


def run_proc(name):
    while True:
        print('%s(%s)' % (name, os.getpid()))


if __name__ == '__main__':
    print('Process (%s) start...' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('子线程将要被启动了')
    p.start()
    p.join()
    print('子线程结束了')
