# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:10:03 2024

@author: Huawei
"""

liste = [1,2,3,4,5]

for i in liste:
    print(i+10)
    
list(map(lambda x : x +10, liste))

liste = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x%2==0, liste))

from functools import reduce

liste = [1,2,3,4]
reduce(lambda a,b : a+b,liste)
