# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:27:45 2020

@author: Ana
"""


# Učitati članove niza. Ispisati članove niza sa
# ideksom koji nije djeljiv sa 4.

niz = []


n = int(input("Unesite broj kojizelite da bude u nizu"))

for i in range(0,n):
    broj = int(input("Unesite broj "))
    niz.append(broj)
    
    
for j in range( n):
    if(niz[j] % 4 != 0):
        print(niz[j])