# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:34:35 2020

@author: Ana
"""

#Napišite program koji će za unesene bodove na testu  ispisati konačnu ocjenu:
#	[0-50> Nedovoljan
#	[50-63> Dovoljan
#	[63-75> Dobar
  #  [75 > 88] vrlo dobar
##	[88-100] Izvrstan
#Ukoliko su bodovi pogrešno uneseni ispisati poruku.

uneseni_bodovi = int(input("Unesite bodove"))

if (uneseni_bodovi < 50):
    print("Ocjena nedovoljan")
elif (uneseni_bodovi >= 50 and uneseni_bodovi < 63):
    print("Dovoljan")
elif (uneseni_bodovi >= 63 and uneseni_bodovi < 75):
    print("Dobar")
elif(uneseni_bodovi >= 75 and uneseni_bodovi < 88):
    print("Vrlo dobar")
elif (uneseni_bodovi >= 88 and uneseni_bodovi <= 100):
    print("Odlican")
else:
    print("krivo uneseni bodovi")