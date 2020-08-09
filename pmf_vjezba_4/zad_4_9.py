# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:45:52 2020

@author: Ana
"""

#Napišite program za testiranje prioriteta operatora u matematičkim izrazima.
#    Program ispisuje poruku “Izračunajte izraz:” i izraz:
#	10%3 != (11//4) + 13 >= True or False
#koliko je korisnik pogodio rješenje, ispisati “Pogodak!”
#ukoliko je pogriješio ispisati “Pogrešan 	unos!” i dodatnu poruku 
#ovisno o tome je li pogodio ili pogriješio tip podatka (brojč
#ani ili logički tip).

#Koje je točno rješenje izraza? Hoćemo li korisnikov uno
#s spremati kao broj ili kao string?

print("Izracunaje izraz 10%3 != (11//4) + 13 >= True or False")

korisnik = input("Odgovor:")
if (korisnik == "34"):
    print("Pogresan tip i unos podatka")
elif (korisnik == "False"):
    print("Pogresan unos ali tocan tip podatka")
elif(korisnik == "True"):
    print("Pogodak")
