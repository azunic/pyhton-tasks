# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 18:02:37 2020

@author: Ana
"""
#Učitati niz X od n članova. Naći maksimum od članova sa parnim indeksima.

niz = []
noviniz = []
n = int(input("Unesite broj"))
for i in range(0,n):
    broj = int(input("Unesite brojeve:"))
    niz.append(broj)
print(niz)
    

najveciclan =niz[0]
for i in range(0,len(niz)):
    if(i % 2 ==0):
        noviniz.append(niz[i])
    print(noviniz)
    
for i in range(0,len(noviniz)):
    if(najveciclan < noviniz[i]):
        najveciclan = noviniz[i]
print(najveciclan)
        
    

                