# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:43:50 2020

@author: Ana
"""

# Učitati  niz od 20 brojeva i ispisati najveći i najmanji broj u nizu.

niz = []
n = int(input("Unesite broj"))
for j in range(0,n):
    broj = int(input("Unesite broj: "))
    niz.append(broj)
 
print(niz)
    

max = niz[0]  
min = niz[0]  
for i in range(1, n):
    if max < niz[i]:    
        max = niz[i]    
    if min > niz[i]:      
        min = niz[i]
print ("Maksimalan clan niza =", max)        
print ("Minimalan clan niza =", min)
