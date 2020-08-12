# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:51:42 2020

@author: Ana
"""

#Kopirajte zadatak 6.5 u novu datoteku. Izmijenite ga na
# način da se korisnika „natjera” da N puta unese dvoznamenkasti broj. 
#Odnosno, da ponovno unese vrijednost ako pogriješi.
N = int(input("Unesite broj"))
while (9 < N < 99):
    N = int(input("Unesite broj"))

lista = []

for i in range(0,N):
    broj=input("Unesite broj")
    lista.append(broj)
    max_broj = lista[0]
    min_broj = lista[0]
    if(max_broj < lista[i]):
        max_broj = lista[i]
print(max_broj)
    
   