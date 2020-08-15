# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:14:46 2020

@author: Ana
"""


# Učitati niz A od n članova. I
#spisati najmanji od njih po apsolutnoj vrijednosti.
# Pri ovome koristiti prvi član niza.


    
niz = []

n = int(input("Unesite brok koliko zelite da vam bude niz:"))

for j in range(0,n):
    broj = int(input("Unesite broj "))
    niz.append(broj)
    prviclan = niz[0]
    
for j in range(0, n):
    if(prviclan > niz[j]):
        prviclan = niz[j]
print(prviclan)
    
apsolutna = abs(prviclan)
print (apsolutna)