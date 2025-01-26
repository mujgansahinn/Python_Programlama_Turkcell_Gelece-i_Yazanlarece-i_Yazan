# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:41:42 2024

@author: Huawei
"""

class VeriBilimci():
    calisanlar =[]
    def __init__(self):
        self.bildigi_diller = []
        self.bolüm = []
    def dil_ekle(self, yeni_dil):
        self.bildigi_diller.append(yeni_dil)
        

ali = VeriBilimci()
ali.bildigi_diller
ali.bolüm

veli = VeriBilimci()
veli.bildigi_diller
veli.bolüm

dir(VeriBilimci)
VeriBilimci.dil_ekle

VeriBilimci.dil_ekle("R")
ali.bildigi_diller("Python")
veli.bildigi_diller("C")
