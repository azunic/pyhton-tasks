# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:57:38 2020

@author: Ana
"""


# Učitati niz X od n članova ispisati one 
#članove niza X koji su veći od prvog (zadnjeg) člana niza.



niz = []
n = int(input("Unesite koliki zelite da vam bude niz"))

for j in range(0,n):
    broj = input("Unesite brojeve: ")
    niz.append(broj)
    pocetni_broj = niz[0]
    print(niz)
    
    
for i in range(0,len(niz)):
    if(pocetni_broj < niz[i]):
        print(niz[i])
        
for i in range(0,n):
    if(niz[i-1] < niz[i]):
        print(niz[i])