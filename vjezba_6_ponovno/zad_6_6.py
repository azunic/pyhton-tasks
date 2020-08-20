# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:29:48 2020

@author: Ana
"""
#Kopirajte zadatak 6.5 u novu datoteku. 
#Izmijenite ga na način da se korisnika „natjera” da N p
#uta unese dvoznamenkasti broj. Odnosno, da ponovno unese 
#vrijednost ako pogriješi.


def Maksmin(N):
    lista = []
    i = 0
    broj = 0
    while (i < N):
        broj = int(input("Unesite dvoznamenkasti broj: "))
        if(broj > 9  and broj < 99):
            lista.append(broj)
            i += 1

    max_broj = lista[0]
    min_broj = lista[0]
    print(lista)
    
    for j in lista:
        if (j > max_broj):
            max_broj = j
        
        if(min_broj > j):
            min_broj = j
    return(max_broj, min_broj)



N = int(input("Unesite dvoznamenkaste brojeve"))

print(Maksmin(N))

   

