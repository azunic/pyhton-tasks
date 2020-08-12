# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:10:23 2020

@author: Ana
"""

#Napišite program u kojem korisnik ponavlja unos sve dok 
#ne unese broj koji je višekratnik broja 7.
a = int(input("Unesite broj"))

while (a % 7 != 0):
    a = int(input("Unesite broj sve dok ne bude visekratnik broja 7"))
    
print("Upjesno")
    
