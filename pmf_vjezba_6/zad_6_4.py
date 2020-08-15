# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:30:23 2020

@author: Ana
"""

#Napišite program u kojem se učit
#ava četveroznamenkasti prirodan broj. P
#rogram treba ispisati je li zbroj prve i čet
#vrte znamenke paran. Korisnik mora ponavljat
#i unos dok ne unese četveroznamenkasti broj. 
#Koristite funkcije: 
#„Znamenkast” koja prima broj i vraća vrijednost „jednoznamenkast”
#
# ili „dvoznamenkast” kao rezultat.
#„i da bude unutar te funkcije koja prima broj i vraća zbroj prve i četvrte znamenke kao rezultat. 
def znamenkast(broj):
    prva_znamenka = broj // 1000
    druga_znamenka = broj % 10
    suma = 0
    suma = prva_znamenka + druga_znamenka
    print(prva_znamenka, druga_znamenka)
    print(suma)
    if (suma % 2==0):
        print("suma je parna")
    else:
        print("Nije parna")
        
        
def provjera_znamenki():
    prva_znamenka = broj // 1000
    druga_znamenka = broj % 10
    
    suma = prva_znamenka + druga_znamenka
    print(prva_znamenka, druga_znamenka)
    print(suma)
    if(suma <= 9):
        print("jednoznamenkasta")
    else:
        print("dvoznamenkasta")
    
    
    

    
broj = int(input("Unesite broj"))
while (broj < 1000 or broj > 9999)):
    broj = int(input("Unesite broj"))
    
znamenkast(broj)
    
provjera_znamenki()