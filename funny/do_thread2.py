# -*- coding: utf-8 -*-
"""
 Created by Monkey at 2019/9/6
"""
import multiprocessing, threading


def loop(increment):
    x = 0
    while True:
        x = x + increment


if __name__ == '__main__':
    print('CPU核数：%s' % multiprocessing.cpu_count())
    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=loop, args=(1, ))
        t.start()
