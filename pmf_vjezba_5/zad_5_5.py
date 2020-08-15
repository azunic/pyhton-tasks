# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 15:05:48 2020

@author: Ana
"""

#Napišite program u kojem korisnik unosi dva 
#broja, a i b koji predstavljaju raspon. Korisn
#ik mora ponavljati unos dok god je a >= b. Progra
#m treba zbrojiti sve elemente unutar zadanog raspona (
#uključujući granice) i ispisati rezultat.

a = int(input("Unesite broj a: "))
b = int(input("Unesite broj b: "))
suma = 0
while (a >= b):
    a = int(input("Unesite broj ponovno a:"))
    b = int(input("Unesite broj ponovno b:"))
    
    
for i in range(a, b + 1):
    suma += i
print(suma)
           
          
