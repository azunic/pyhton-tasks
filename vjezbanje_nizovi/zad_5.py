# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:29:31 2020

@author: Ana
"""


# Učitati članove niza. Ispisati članove niza sa p
#arnom vrijednosti (djeljive sa 2).

lista = []


n = int(input("Unesite brojeve: "))

for i in range(0,n):
    broj = int(input("Unesite broj"))
    lista.append(broj)
    
    
for j in range(n):
    if( niz[j] % 2 ==0):
        print(niz[j]