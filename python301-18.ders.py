# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:26:47 2024

@author: Huawei
"""

maaslar = [1000,2000,3000,4000,5000]

    def maas_üst(x):
        print(x*10/100 +x)

    def maas_alt(x):
        print(x*20/100 +x)
for i in maaslar:
    if i >= 3000:
        maas_üst(i)
    else:
        maas_alt(i)