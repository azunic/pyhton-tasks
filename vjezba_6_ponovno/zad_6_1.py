# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 15:40:16 2020

@author: Ana
"""

#Napišite program u kojem korisnik unosi broj N. Program 
# tražiti od korisnika da unese N cijelih brojeva i ispisati 
#njihovu aritmetičku sredinu. 
#Koristite funkciju „ArtimetickaSredina” koja prima broj i vraća rezultat.

def aritmetickasredina(N):
    
    suma = 0
    
    for i in range(0, N):
        broj = int(input("Unesite brojeve"))
        suma += broj
    print(suma)
    sredina = suma / N
    return(sredina)
    
    
N = int(input("Unesite broj "))

print(aritmetickasredina(N))