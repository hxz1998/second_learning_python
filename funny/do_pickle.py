# -*- coding: utf-8 -*-
"""
 Created by Monkey at 2019/9/5
"""
import pickle
import unittest


class PickleTest(unittest.TestCase):
    def test_base(self):
        d = dict(name='Bob', age=20, score=88)
        print(pickle.dumps(d))
        with open('./1.txt', 'wb') as f:
            # f.write(pickle.dumps(d))
            pickle.dump(d, f)

    def test_opendict(self):
        with open('./1.txt', 'rb') as f:
            d = pickle.load(f)
            f.close()
            print(d)
