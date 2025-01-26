# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:34:52 2024

@author: Huawei
"""

maaslar = [8000,5000,2000,1000,3000,7000,1000]
dir(maaslar)
maaslar.sort()
maaslar

for i in maaslar:
    if i ==3000:
        print("kesildi")
        break
    print(i)
    
 for i in maaslar:
     if i ==3000:
         print("kesildi")
         continue
     print(i)   
