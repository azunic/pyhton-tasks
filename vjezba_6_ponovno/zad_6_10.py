# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 15:32:48 2020

@author: Ana
"""

#Napišite program u kojem korisnik unosi rečenicu. 
#Svaku pojavu riječi “kupus” treba zamijeniti riječju
# “kelj”. Ispisati novu rečenicu.
#	Napomena: riječ kupus mora biti samostalna riječ



string  = input("Unesie recenicu: ")
novistring = string.split()
print(novistring)

rezultat = ""
for rijec in novistring:
    if (rijec == "kupus"):
        rezultat += "kelj "
    else:
        rezultat += (rijec + ' ')
print(rezultat)
    
    
# ana kupus kelj ana ne slusa nista zivo kupuskusus
