# coding:utf-8

"""
    @version:  python2.7
    @date:     2017/3/19 下午6:16
    @file:     learn-pickle.py
    @software: PyCharm
    @auther:   Aesthetic92
"""

from __future__ import unicode_literals
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import cPickle

lines = [
    "I'm like a dog chasing cars.",
    "I wouldn't know what to do if I caught one...",
    "I'd just do things."
]

with open('../data/lines.pkl', 'w') as f: 	# 序列化并保存成文件
    cPickle.dump(lines, f)

with open('../data/lines.pkl', 'r') as f: 	# 从文件读取并反序列化
    lines_back = cPickle.load(f)

print(lines_back)                   	# 和lines一样
print lines_back[1]

obj = 123, "abcdedf", ["ac", 123], {"key": "value", "key1": "value1"}
data_string = cPickle.dumps(obj)
print data_string

print type(data_string)

string_data = cPickle.loads(data_string)
print string_data
print type(string_data)


print '{}, {}test.'.format(18,19)
#print os.listdir('..')

