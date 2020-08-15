# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:48:47 2020

@author: Ana
"""

#Napišite program u kojem će korisnik unijeti duljinu u metrima.
#	Pomoću izbornika, nuditi korisniku opcije:
#	1. Pretvorba unesene duljine u milimetre
#	2. Pretvorba unesene duljine u centimetre
#	3. Pretvorba unesene duljine u kilometre
#	4. Novi unos duljine
#	5. Kraj.
#	Ukoliko korisnik ne unese neku od navedenih opcija 	ispisati “Niste dobro unijeli opciju.”.
#


broj_u_metrima = int(input("Unesite duljinu u metrima: "))
 
milimetri = 0
centrimetri = 0
kilometri = 0
print("IZBORNIK" )
print ("Pomoću izbornika, nuditi korisniku opcije:")
print("1. Pretvorba unesene duljine u milimetre")
print("2. Pretvorba unesene duljine u centimetre")
print("3. Pretvorba unesene duljine u kilometre")
print("4. Novi unos duljine")
print("5. Kraj")

korisnik = 0
while(korisnik != 5):
    
    korisnik = int(input("Unesite broj "))

    if(korisnik == 1):
        milimetri = broj_u_metrima * 10000
        print("Milimetri: ", milimetri)
    elif(korisnik == 2):
        centimetri = broj_u_metrima * 100
        print("centimetri: ", centimetri)
    elif(korisnik == 3):
        kilometri = broj_u_metrima / 1000
        print("kilometri: ", kilometri)
    elif(korisnik == 4):
        broj_u_metrima = int(input("Unesite duljinu u metrima: "))
        
        
print("kraj")