#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/9/11 下午3:23
@Author  : fanyuexiang
@Site    : 
@File    : test.py
@Software: PyCharm
@version: 1.0
@describe: 项目测试用例
'''
from dataformate import get_knn_data

filepath = 'dataset/KNNData.txt'
name = ['fly distance', 'play time', 'ice cream', 'like level']
df = get_knn_data(filepath, names=name)
print(df)