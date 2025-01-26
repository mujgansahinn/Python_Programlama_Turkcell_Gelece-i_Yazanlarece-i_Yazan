# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:02:35 2024

@author: Huawei
"""

a = [1,2,3,4]
b = [2,3,4,5]
ab = []

for i in range(0, len(a)):
    ab.append(a[i]*b[i])
    print(i)
ab

import numpy as np 
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
a*b
