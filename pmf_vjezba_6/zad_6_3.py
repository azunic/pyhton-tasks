# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:17:00 2020

@author: Ana
"""

#Napišite program koji će tražiti od 
#korisnika da ponavlja unos dok god ne unese če
#tveroznamenkasti broj. Program na kraju ispisuj
#e broj kojega je korisnik unio.
#Koristite funkciju „Unos” koja ne prima parametre i vraća vrijednost.

broj = int(input("Unesite broj"))

while(999 >= broj < 1000):
    broj=int(input("Unesite broj ponovno"))
    
print("Broj je u redu")
    

    
