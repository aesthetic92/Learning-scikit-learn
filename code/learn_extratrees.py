# coding:utf-8

"""
    @version:  python2.7
    @date:     2017/4/4 下午2:14
    @file:     learn_extratrees.py
    @software: PyCharm
    @auther:   Aesthetic92
"""

from __future__ import unicode_literals
import sys

reload(sys)
sys.setdefaultencoding('utf8')

import numpy as np
import urllib

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=',')
print dataset.shape

X = dataset[:, 0:7]
y = dataset[:, 8]
print X[:3]

from sklearn import preprocessing
scaled_X = preprocessing.scale(X)
print scaled_X[:3]
normalized_X = preprocessing.normalize(X)
print normalized_X[:3]

from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier

model = ExtraTreesClassifier()
model.fit(X, y)
print model.feature_importances_
