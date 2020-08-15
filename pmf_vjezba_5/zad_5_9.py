# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:39:12 2020

@author: Ana
"""

#Napišite program u kojem korisnik ponavlja unos sve dok ne
# unese troznamenkasti broj.

x=int(input("Unesite broj: "))
while (x < 100 or x > 1000):
    x = int(input("Unesite troznamenaksti broj: "))
    
print("Bravo unijeli ste troznamenkasti broj")
