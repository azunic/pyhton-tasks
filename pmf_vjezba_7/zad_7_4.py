# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:49:16 2020

@author: Ana
"""

#Napišite program u kojem korisnik unosi broj 
#za koji je potrebno ispisati je li prost broj.
#U rasponu od 1 do samog broja uključivo, prosti brojevi 	
#djeljivi su samo sa 1 i samim sobom.
#	Ograničenje ulaza: uneseni broj x ∈ [1,100]
#Koristite funkciju „Prost” koja prima broj i vraća bool vrijednost (True ili False) ovisno o tome je li broj prost ili ne.

def Prost(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


n=0
while (n < 1 or n > 100):
    n = int(input("Unesite broj:"))

print(Prost(n))
if (Prost(n)):
    print("Prost je")
else:
    print("Nije prost")