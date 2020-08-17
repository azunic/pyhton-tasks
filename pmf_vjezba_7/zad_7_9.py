# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:56:41 2020

@author: Ana
"""

#da li je rijec palindrom


string = "rotor"
novi = ''
for i in string:
    novi += i
    print(novi)
if string == novi:
    print("Tocno")
else:
    print("Nije tocno")
    