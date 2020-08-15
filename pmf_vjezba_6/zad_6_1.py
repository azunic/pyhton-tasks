# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:38:32 2020

@author: Ana
"""

#Napišite program u kojem korisnik unosi broj N. Progra
#m treba tražiti od korisnika da unese N cijelih brojeva i 
#ispisati njihovu aritmetičku sredinu. 
#Koristite funkciju „ArtimetickaSredina” koja prima broj i vraća rezultat.


def aritmetickasredina(N, suma):
      sredina = 0
      sredina = suma / N
      return (sredina)
      

N = int(input("Unesite N cijelih brojeva"))

suma = 0
for i in range(0, N):
    brojevi = int(input("Unesite brojeve"))
    suma += brojevi


print(aritmetickasredina(N, suma))