"""
    Created by Xiaozhong.
    Copyright (c) 2019/9/6 Xiaozhong. All rights reserved.
"""
import hashlib, hmac

md5 = hashlib.md5()
sha1 = hashlib.sha1()
md5.update('how to use md5'.encode('utf-8'))
print(md5.hexdigest())

md5.update('how to use md6'.encode('utf-8'))
print(md5.hexdigest())

message = b'nihao'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())
