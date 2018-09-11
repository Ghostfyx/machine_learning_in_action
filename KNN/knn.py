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

filepath = '../dataset/KNNData.txt'
name = ['fly distance', 'play time', 'ice cream', 'like level']
df = get_knn_data(filepath, names=name)
labelset = set(df.iloc[:, -1])

# 使用matplotlab绘制散点图
plt.scatter()