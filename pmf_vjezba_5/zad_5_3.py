# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 17:36:24 2020

@author: Ana
"""

#Napišite program u kojem će program zbrajati pr
#irodne brojeve dok god suma ne postane veća od broja 
#x. Broj x unosi korisnik. Program treba ispisati koliko
# je prirodnih brojeva zbrojeno


suma=0
x = int(input("Unesite broj"))
counter_brojeva = 0
while (suma < x):
    a = int(input("Unesite broj"))
    suma += a
    counter_brojeva += 1
print(suma)
print(counter_brojeva)
    