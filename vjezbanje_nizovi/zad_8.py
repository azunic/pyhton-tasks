# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:50:14 2020

@author: Ana
"""


#Učitati niz X od n članova ispisati one članove niza X koj
#i su veći od prvog (zadnjeg) člana niZA.
lista = []
n = int(input("Unesite niz"))

for j in range(0,n):
    broj = int(input("Unesite niz"))
    lista.append(broj)
    
    pocetni_niz = lista[0]
    
    
for j in range(0, n):
    if(pocetni_niz < niz[j]):
        print(niz[j])