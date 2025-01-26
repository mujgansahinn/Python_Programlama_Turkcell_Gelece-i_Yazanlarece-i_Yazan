# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 23:38:04 2024

@author: Huawei
"""

a = 10
b = 0
a/b
try:
    print(a/b)
except ZeroDivisionError:
    print("paydada sıfır olmaz")
    
a=10
b="2"
try:
    print(a/b)
except TypeError:
    print("sayı ve string problemi")