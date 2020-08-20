# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:09:46 2020

@author: Ana
"""

#Napišite program u kojem se učitava prirodan broj, ko
#ji se zatim ispisuje u inverznom (obrnutom) poretku znamenaka. 
#Ne pretvarati početni broj u string.
#Koristite funkciju „Obrni” koja prima jedan broj i 
#vraća broj u inverznom poretku.
   
def Obrni(broj):
    reverse = 0
    
    while broj > 0:
        znamenka = broj % 10 
        reverse = reverse * 10 + znamenka 
        broj = broj // 10
    print(reverse)

broj = int(input("Unesite  broj: "))

Obrni(broj)
