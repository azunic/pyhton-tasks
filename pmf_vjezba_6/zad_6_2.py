# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:04:29 2020

@author: Ana
"""

#Napišite program u kojem će se uč
#itati cijeli broj. Ukoliko je unesen četve
#roznamenkasti broj ispisati da li mu je suma prv
#e i četvrte znamenke paran broj (suma jedinica i tisući
#ca). Ukoliko broj nije četveroznamenkast, ispisati poruku „U
#neseni broj nije 4-znamenkast”.

#Koristite funkciju „Provjera” koja prima broj i ne vraća vrijednost.

def provjera(broj):
    
    zadnja_znamenka = broj%10
    prva_znamenka = broj//1000
    print(zadnja_znamenka,prva_znamenka)
    
    if (1000 < broj <9999):
        print("broj ima 4 znamneke")
        suma = zadnja_znamenka + prva_znamenka
        if (suma % 2 ==0):
            print("suma je paran broj")
        
    
        
    else:
        print("Uneseni broj nije cetveroznamenkast")





broj = int(input("Unesite broj"))

provjera(broj)