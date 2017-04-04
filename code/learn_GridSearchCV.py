# coding:utf-8

"""
    @version:  python2.7
    @date:     2017/4/4 下午5:51
    @file:     learn_GridSearchCV.py
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

from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

alphas = np.array([1, 0.1, 0.01, 0.001, 0.0001, 0])
model = Ridge()
grid = GridSearchCV(estimator=model, param_grid=dict(alpha=alphas))
grid.fit(X, y)
print 'grid'
print grid

print 'grid best score'
print grid.best_score_

print 'grid best estimator alpha'
print grid.best_estimator_.alpha
