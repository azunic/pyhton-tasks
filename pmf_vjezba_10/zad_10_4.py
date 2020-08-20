# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:51:35 2020

@author: Ana
"""

#Napišite program u kojem korisnik unosi n prirodnih brojeva 
#u niz Pozitivni (provjeravati korisnikov unos svaki put i osi
#gurati da su u niz uneseni samo ispravni brojevi). 
#	Parne brojeve iz niza Pozitivni smjestiti u niz Parni, a 	
#neparne u Neparni.
#	Ispisati nizove Pozitivni, Parni i Neparni.

n = int(input("Unesite n prirodnih brojeva: "))
pozitivna = n*[]
parni = []
neparni =[]

i = 0
    
while(i < n):
    broj = int(input("Unesite broj"))
    while(broj < 0):
        broj = int(input("Unesite broj ponovo"))
    pozitivna.append(broj)
    i +=1
print(pozitivna)

for j in range(0,len(pozitivna)):
    print(pozitivna[j])     
    if (pozitivna[j] % 2 ==0):
        parni.append(pozitivna[j])
    else:
        neparni.append(pozitivna[j])
print(parni,neparni)