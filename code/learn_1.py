# coding:utf-8

"""
    @version:  python2.7
    @date:     2017/4/3 下午11:40
    @file:     learn_1.py
    @software: PyCharm
    @auther:   Aesthetic92
"""

from __future__ import unicode_literals
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
from numpy import *

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.ones(3)
c = np.array([[1,2,3,1],[4,5,6,1],[7,8,9,1]])

print '*'*40
print np.c_[a,b]
print np.c_[a,a]
print np.c_[b,a]
# print np.r_[a,b]  # error, a,b must have same number of dimensions.

print '*'*40
print np.insert(a, 0, values=b, axis=1)
print np.insert(a, 3, values=b, axis=1)
print np.insert(a, 3, values=b, axis=0)

print '*'*40
print np.column_stack((a,b))
print np.row_stack((a,b))