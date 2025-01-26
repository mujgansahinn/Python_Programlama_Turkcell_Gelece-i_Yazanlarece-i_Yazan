# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:35:46 2024

@author: Huawei
"""

class LineCounter:
    def __init__(self,filename):
        self.file = open(filename, "r")
        self.lines = []
    
    def read(self):
        self.lines = [lines for line in self.file]
        
    def count(self):
        return len(self.lines)

lc= LineCounter("deneme.txt")

print(lc.lines)
print(lc.count())