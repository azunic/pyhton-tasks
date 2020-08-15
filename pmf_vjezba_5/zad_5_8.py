# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:35:37 2020

@author: Ana
"""

#Napisati program koji će na ekran ispisati s
#ve brojeve koji su djeljivi sa 3, a nisu djelj
#ivi sa 7 između 100 i 1000 (uključene granice).

for i in range(100, 1001):
    if (i % 3 == 0 and i % 7 != 0):
        print(i)
        
