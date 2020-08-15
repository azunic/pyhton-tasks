# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:05:26 2020

@author: Ana
"""

#Napišite program u kojem računalo sl
#učajno generira dvoznamenkasti broj kojem je zbroj znamenki neparan broj.
import random


suma = 0
broj = random.randint(1,99)
while (suma % 2 ==0):
    broj = random.randint(1,99)
    print(broj)
    prva_znamenka = broj // 10
    druga_znamenka = broj % 10
    print(prva_znamenka,druga_znamenka)
    suma = prva_znamenka + druga_znamenka
print("Suma je neparna i zavrsi program")  

    
