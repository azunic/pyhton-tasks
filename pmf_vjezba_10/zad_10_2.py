# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 23:33:08 2020

@author: Ana
"""

#Napišite program u kojem korisnik unosi n riječi u niz Rijeci. 
#	Za svaku riječ iz niza ispisati broj samoglasnika koji se 	p
#ojavljuje u njoj.

n = 5
lista = []
brojac = 0

for i in range(0, n):
    rijec = input("Unesite string")
    lista.append(rijec)
print(lista)

for j in lista:
   print (j)
   for i in j:
       print(i)
       if (i in "aeiou"):
           brojac+=1
   print(brojac)