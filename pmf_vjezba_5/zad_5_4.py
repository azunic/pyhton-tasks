# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:42:40 2020

@author: Ana
"""


#Napišite program u kojem korisnik unosi deset brojeva. Ispi
#sati umnožak brojeva, sumu parnih i sumu neparnih brojeva.


suma = 0
suma_neparnih = 0
mnozenje = 1
for i in range(0, 10):
    x = int(input("Unesite ", i + 1, ". broj"))
    mnozenje = mnozenje * x

    if (x % 2 == 0):
        suma += x
    else:
        suma_neparnih += x
        
print(mnozenje,suma,suma_neparnih)