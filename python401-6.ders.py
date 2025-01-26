# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:52:35 2024

@author: Huawei
"""

class employees():
    def __init__(self):
        self.FistName = ""
        self.LastName = ""
        self.adress = ""
        
class datascientists(employees):
    def __init__(self):
        self.programming= ""
veribilimci1 = datascientists()
veribilimci1

class marketing(employees):
    def __init__(self):
        self.storytellers = ""
        
        
class employee_yeni():
    def __init__(self,firstname,lastname,address):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
ali=employee_yeni("a","b","c")
ali.firstname
ali.lastname        
ali.address 

       
    