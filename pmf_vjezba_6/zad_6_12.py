# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:59:52 2020

@author: Ana
"""

#Napisati program koji će unijeti ime datoteke s ekstenzijom. 
#	Ispisati poruku o vrsti datoteke: „Naziv.txt je tekstualna 	
#datoteka“ (npr. tekstualna (txt), muzička (mp3), 	grafička
# (jpg), ostale vrste datoteka).
#	Ispisati upozorenje ukoliko se u nazivu datoteke nalaze 	
#nedopušteni znakovi: 
#	\ / : * ? " < > | 

ime_datoteke = input("Unesite ime datoteke")

provjera_zadnja_tri = ime_datoteke[-3:]
print(provjera_zadnja_tri)