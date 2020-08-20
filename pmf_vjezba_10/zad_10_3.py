# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:06:50 2020

@author: Ana
"""
#Napišite program u kojem korisnik unosi prirodne brojeve u niz Brojevi sve dok ne unese 0.
#	Ispisati minimalni element niza i njegovu poziciju.
#	Ispisati maksimalni element niza i njegovu poziciju.
#	Ako ima više istih elemenata, ispisati sve brojeve
lista = []

broj = int(input("Unesite broj"))

while broj != 0:
    broj = int(input("Unesite broj:"))
    if (broj == 0):
        continue
    else:
        lista.append(broj)
print(lista)
    
minlista = lista[0]
maxlista = lista[0]
for i in range(0,len(lista)):
    if (minlista > lista[i]):
        minlista = lista[i]
    if (maxlista < lista[i]):
        maxlista = lista[i]
        
for i in range(0,len(lista)):
    if(minlista ==lista[i]):
        print("Minimalna pozicija je:",i)
    if (maxlista ==lista[i]):
        print("Maksimalna pozicija je:", i)
print("Minimalan broj je:" ,minlista)
print("a maksimalan broj je:", maxlista)