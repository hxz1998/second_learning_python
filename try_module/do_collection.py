"""
    Created by Xiaozhong.
    Copyright (c) 2019/9/6 Xiaozhong. All rights reserved.
"""
from collections import namedtuple, deque, defaultdict, OrderedDict, ChainMap, Counter
import os, argparse
import base64

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p)
print(p.x)

q = deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('z')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'aaa'
print(dd.items())
print(dd['key2'])

od = OrderedDict()
od['a'] = 1
od['b'] = 2

print(list(od.keys()))

defaults = {
    'color': 'red',
    'user': 'guest'
}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
print(vars(namespace))
command_line_args = {k: v for k, v in vars(namespace).items() if v}

print(command_line_args)
combined = ChainMap(command_line_args, {}, defaults)
print(combined)
print('color=%s\nuser=%s' % (combined['color'], combined['user']))

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)

print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))