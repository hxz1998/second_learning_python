"""
    Created by Xiaozhong.
    Copyright (c) 2019/9/6 Xiaozhong. All rights reserved.
"""
from contextlib import contextmanager
from urllib.request import urlopen


class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('Bob') as q:
    q.query()


class Query2():

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('begin')
    q = Query2('nihao')
    yield q
    print('End')


with create_query('Bob') as q:
    q.query()


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()


with closing(urlopen('https://baidu.com')) as page:
    for line in page:
        print(line)
