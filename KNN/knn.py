#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/9/11 下午3:22
@Author  : fanyuexiang
@Site    : 
@File    : knn.py
@Software: PyCharm
@version: 1.0
@describe: 构建KNN模型
'''
from pprint import pprint

from dataformate import get_knn_data
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

filepath = '../dataset/KNNData.txt'
name = ['fly distance', 'play time', 'ice cream', 'like level']
df = get_knn_data(filepath, names=name)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
# 对数据进行标准化处理
sc = StandardScaler()
X_std = sc.fit_transform(X)
# 使用matplotlab绘制散点图
plt.scatter(X[y==1, 0], X[y==1, 1], color='red', marker='^', alpha=0.5)
plt.scatter(X[y==2, 0], X[y==2, 1], color='blue', marker='*', alpha=0.5)
plt.scatter(X[y==3, 0], X[y==3, 1], color='green', marker='o', alpha=0.5)
plt.show()