# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:20:47 2020

@author: Ana
"""

#. Učitati članove niza. Ispisati članove niza sa parnim indeksom.

niz = []


n = int(input("Unesite broj kojizelite da bude u nizu"))

for i in range(0,n):
    broj = int(input("Unesite broj "))
    niz.append(broj)
    
    
for j in range( n):
    if(niz[j] % 2==0):
        print(niz[j])
    