# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:34:36 2020

@author: Ana
"""

#Napisati program koji će unijeti ime datoteke s ekstenzijom. 
#
#	Ispisati poruku o vrsti datoteke: „Naziv.txt je tekstualna 	
#datoteka“ (npr. tekstualna (txt), muzička (mp3), 	grafička (jpg),
# ostale vrste datoteka).
#	Ispisati upozorenje ukoliko se u nazivu datoteke nalaze 	
#nedopušteni znakovi: 
    
#	\ / : * ? " < > | 



ime_datoteke = input("Unesite puno ime datoteke s ekstenzijom: ")
losi_znakovi = "\\/:*?<>|"
ekstenzija = ime_datoteke[-3:]
naziv = ime_datoteke[0:-4]
print("naziv", naziv)
print("ekstenzija", ekstenzija)


greska = False
for slovo in naziv:
    if (slovo in losi_znakovi):
        greska = True
            
if(greska):
    print("Pogresan naziv!")
else:
    if(ekstenzija == 'txt'):
        print(ime_datoteke, "je tekstualna datoteka!")
        
    
