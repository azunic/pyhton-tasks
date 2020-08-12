# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:00:49 2020

@author: Ana
"""

#Napišite program u kojem računalo slučajno gener
#ira dvoznamenkasti broj kojem je zbroj znamenki neparan broj.
import random

broj = random.randint(9,99)
prvi_broj = broj // 10
drugi_broj = broj %10
suma = prvi_broj+ drugi_broj
print(prvi_broj, drugi_broj)
if(suma % 2 !=0):
    print(broj, "Broj je neparan")
else:
    broj = random.randint(9,99)
    print(broj, "Broj je paran")

//DRUGI NACIN 
import random 

broj1 = random.randrange(9,100,2)

prva_znamenka = round(broj1 /10) 
druga_znamenka = broj1 % 10 

suma = prva_znamenka + druga_znamenka
print(broj1,prva_znamenka,druga_znamenka,suma)
