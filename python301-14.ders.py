# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:49:11 2024

@author: Huawei
"""

sinir = 50000
magaza_adi = input("Mağaza adı nedir? ")
gelir = int(input("Gelirinizi Giriniz: "))

if gelir > sinir : 
    print("Tebrikler, promosyon kazandınız!")
elif gelir < sinir :
    print("Uyarı!")
else:
    print("Takibe devam")

sinir = 50000
magaza_adi = input("Mağaza adı nedir? ")
gelir = int(input("Gelirinizi Giriniz: "))

if gelir > sinir : 
    print("Tebrikler: "+ magaza_adi+ " promosyon kazandınız!")
elif gelir < sinir :
    print("Uyarı! Çok düşük gelir: " + str(gelir))
else:
    print("Takibe devam")