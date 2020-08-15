# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:48:54 2020

@author: Ana
"""

#pronaci najmanji clan niza


# Učitati članove i naći najmanji član niza.
lista = []
n = int(input("Unesite broj niza"))

for j in range(0,n):
    broj = int(input("Unesite broj: "))
    lista.append(broj)
    
    
pocetni_clan = lista[0]

print(pocetni_clan)
for i in range(1,n):
    if(pocetni_clan  > lista[i]):
        pocetni_clan = lista[i]
print(pocetni_clan)
        