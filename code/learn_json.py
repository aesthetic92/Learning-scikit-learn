# coding:utf-8

"""
    @version:  python2.7
    @date:     2017/5/25 下午11:09
    @file:     learn_json.py
    @software: PyCharm
    @auther:   Aesthetic92
"""

from __future__ import unicode_literals
import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')

# 编码：把一个Python对象编码转换成Json字符串   json.dumps()
# 解码：把Json格式字符串解码转换成Python对象   json.loads()

# dumps方法有几个比较有用的参数：sort_keys控制是否排序（True or False），indent定义缩进大小（int类型），
# separators是一个元组，定义分隔符的类型。

data1 = {'b':789, 'c':456, 'a':123}
data2 = {'a':123, 'b':789, 'c':456}
d1 = json.dumps(data1, sort_keys=True)
d2 = json.dumps(data2)
d3 = json.dumps(data2, sort_keys=True)
print d1
print d2
print d3
print d1 == d2

data1 = {'b':789, 'c':456, 'a':123}
d1 = json.dumps(data1, sort_keys=True, indent=4)
print d1

a = ['foo', {'bar': ('baz', None, 1.0, 2)}]
b = json.dumps(a)
print b
c = json.loads(b)
print c
