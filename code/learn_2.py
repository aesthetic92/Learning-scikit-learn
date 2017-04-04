# coding:utf-8

"""
    @version:  python2.7
    @date:     2017/4/4 上午12:17
    @file:     learn_2.py
    @software: PyCharm
    @auther:   Aesthetic92
"""

from __future__ import unicode_literals
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import pandas as pd
from pandas import DataFrame

df = DataFrame(np.random.randn(4, 5), columns=['A', 'B', 'C', 'D', 'E'])

# print df.dtypes
# print df
# df['A'] = df['A'].astype(int)
# print df.dtypes
# print df

print df
print df.loc[1]
print df['B']
print df.shape
df['F'] = [1, 2, 3, 4]
print df.shape