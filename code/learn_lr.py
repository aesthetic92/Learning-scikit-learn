# coding:utf-8

"""
    @version:  python2.7
    @date:     2017/4/4 下午2:14
    @file:     learn_lr.py
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

from sklearn import metrics
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X, y)
print 'model'
print model

print 'result'
print metrics.classification_report(y, model.predict(X))

print 'confusion matrix'
print metrics.confusion_matrix(y, model.predict(X))
