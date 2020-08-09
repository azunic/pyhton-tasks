# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:23:04 2020

@author: Ana
"""

#Napišite program koji će zbrojiti prvih N broje
#va, uključujući N. Korisnik unosi N. Program tre
#ba ispisati sumu. 

N = int(input("Unesite n brojeve"))

zbroj = 0
for i in range(0, N + 1):
    zbroj += i
print(zbroj)




