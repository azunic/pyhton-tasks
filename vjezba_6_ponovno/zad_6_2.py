# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:03:02 2020

@author: Ana
"""

#Napišite program u kojem će se učitati cijeli broj.
# Ukoliko je unesen četveroznamenkasti broj ispisati
# da li mu je suma prve i četvrte znamenke paran bro
#j (suma jedinica i tisućica). Ukoliko broj nije četv
#eroznamenkast, ispisati poruku „Uneseni broj nije 4-znamenkast”.

#Koristite funkciju „Provjera” koja prima broj i ne vraća vrijednost.
#



def provjera(broj):
    
    suma = 0
    prva_znamenka = broj //1000
    zadnja_znamenka = broj % 10
    print(prva_znamenka, zadnja_znamenka)
    if(broj >=999 and broj < 9999):
        suma = prva_znamenka + zadnja_znamenka
        if (suma % 2 ==0):
         print("Suma je: ", suma)

    else:
        print("Uneseni broj nije cetveroznamenkast")
        
   

broj= int(input("Unesite broj"))    
provjera(broj)