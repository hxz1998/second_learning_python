# -*- coding: utf-8 -*-
"""
 Created by Monkey at 2019/9/5
"""
import unittest


class IOTest(unittest.TestCase):
    def test_base_io(self):
        with open('./test.txt', 'wb') as f:
            f.write('z你好'.encode('utf-8'))

    def test_stringio(self):
        from io import StringIO
        f = StringIO('hello\nHi!')
        while True:
            s = f.readline()
            if s == '':
                break
            print(s.strip())

    def test_bytesio(self):
        from io import BytesIO
        f = BytesIO()
        f.write('中文'.encode('utf-8'))
        print(f.getvalue())


if __name__ == '__main__':
    unittest.main()
