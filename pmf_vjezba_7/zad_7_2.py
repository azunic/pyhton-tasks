# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:21:35 2020

@author: Ana
"""

#Napišite program koji će za uneseni broj i
#spisati sumu i broj njegovih znamenki (npr. za 
#uneseno 324 ispisuje se 9 i 3).
#Koristiti funkciju „BrojZnamenki” koja prima
# broj i vraća jedan broj kao rezultat

def BrojZnamenki(broj):
    
    suma = 0
    brojac = 0
    while broj > 0:
        suma += broj % 10
        broj/= 10
        broj = int(broj)
        brojac +=1
    return(suma,brojac)

   





broj = int(input("Unesite broj: "))
print(BrojZnamenki(broj))

