# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:02:07 2020

@author: Ana
"""

#Napišite program u kojem korisnik unosi N 
#dvoznamenkastih brojeva. Korisnik unosi N. P
#rogram treba ispisati najveći i najmanji broj. 
#Koristite funkciju „MaksIMin” koja prima vrijednost N 
#i ne vraća rezultat. Funkcija mora ispisati najveći i na
#jmanji broj koje je korisnik unio. 
#Koristite funkcije „Maks” i „Mini” koje primaju dva broja i vraćaju ve
#ći (maks), odnosno manji (mini), od njih dva.

def Maksmin(N):
    lista = []
    
    for i in range(0,N):
        broj = int(input("Unesite dvoznamenkasti broj: "))
        lista.append(broj)
        max_broj = lista[0]
        min_broj = lista[0]
    print(lista)
    
    for j in lista:
        if (j > max_broj):
            max_broj = j
        
        if(min_broj > j):
            min_broj = j
    return(max_broj, min_broj)



N = int(input("Unesite dvoznamenkaste brojeve"))

print(Maksmin(N))