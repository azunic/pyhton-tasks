# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 21:39:16 2020

@author: Ana
"""
#Učitati niz X od n članova.
# Naći minimum i  maksimum  od 
#članova sa indeksima djeljivim sa 3.
niz = []
noviniz = []
n = int(input("Unesite broj"))
for i in range(0,n):
    broj = int(input("Unesite brojeve:"))
    niz.append(broj)
print(niz)
    
for i in range(0,len(niz)):
    if(i % 3==0):
        noviniz.append(niz[i])
print(noviniz)

najveciclan = noviniz[0]

for i in range(0,len(noviniz)):
    if(najveciclan < noviniz[i]):
        najveciclan = noviniz[i]
print(najveciclan)