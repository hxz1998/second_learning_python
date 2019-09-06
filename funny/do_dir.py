# -*- coding: utf-8 -*-
"""
 Created by Monkey at 2019/9/5
"""
import unittest

class DirTest(unittest.TestCase):

    def test_dir(self):
        import os
        print(os.name)
        print(os.environ)
        print(os.path.abspath('.'))
        path = os.path.abspath('.')
        print(os.path.split(path))
        path = os.path.join(path, 'new_dir')
        os.mkdir(path)

    def test_filter(self):
        import os
        print([x for x in os.listdir('../') if os.path.isdir(x)])



if __name__ == '__main__':
    unittest.main()