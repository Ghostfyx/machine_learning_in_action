#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Time    : 2018/9/11 下午3:15
@Author  : fanyuexiang
@Site    : 
@File    : dataformate.py
@Software: PyCharm
@version: 1.0
@describe: 对数据集的数据读取，并进行数据预处理
'''
import pandas as pd

def get_knn_data(filename, names):
    """
    KNN的各列数据均为离散型变量，类别标注已经进行了处理
    :param filename:
    :param names:
    :return:
    """
    df = pd.read_csv(filename, header=None, sep='\t', names=names)
    return df