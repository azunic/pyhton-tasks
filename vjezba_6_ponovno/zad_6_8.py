# -#*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:13:06 2020

@author: Ana
"""

#Napišite program za “Igru pogađanja broja”.
#Program bira slučajan broj [1,100], a korisnik unosi 
#brojeve sve dok ne pogodi slučajni broj. Kod svakog unosa, 
#ispisuje se poruka o tome je li uneseni broj manji ili veći 
#od “zamišljenog” broja. Također, na kraju se ispisuje 
#broj pokušaja pogađanja.
import random
i=0
broj = random.randint(1,100)
print(broj)

korisnik_unos = 0

while(korisnik_unos != broj):
    korisnik_unos = int(input("Unesite broj: "))
    i += 1
    if(korisnik_unos < broj):
        print("Broj je veci od vaseg unosa")
    else:
        print("Broj je manji od vaseg unosa")
print("Broj pokusaja pogadanja je:", i, "Bravo uspjeli ste")

