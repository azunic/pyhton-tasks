# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:11:12 2020

@author: Ana
"""

#Učitati članove niza. Ispisati: članove niza
# koji su veći od slijedećeg člana.


niz = []

N = int(input("Unesite broj"))

for j in range(0, N):
    broj = int(input("Unesite broj "))
    niz.append(broj)
    

for i in range(0,N -1):
    if(niz[i] > niz[i+1]):
        print(niz[i])
        