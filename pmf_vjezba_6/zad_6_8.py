# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:10:21 2020

@author: Ana
"""

#Napišite program za “Igru pogađanja broja”.
#Program bira slučajan broj [1,100], a korisnik unosi b
#rojeve sve dok ne pogodi slučajni broj. Kod svakog unosa, 
#ispisuje se poruka o tome je li uneseni broj manji ili veći o
#d “zamišljenog” broja. Također, na kraju se ispisuje broj pokušaja pogađanja.
import random
brojac = 0
broj = int(input("Unesite broj"))

komp = random.randint(1,100)
print(komp)

while (broj != komp):
    broj = int(input("Unesite broj"))
    brojac+=1
    if (broj < komp):
        print("broj je manji od broja od racunala")
    else:
        print("Broj je veci od racunalovog broja")
    
print("Bravo pogodili ste broj i broj pokusaja je bio", brojac)