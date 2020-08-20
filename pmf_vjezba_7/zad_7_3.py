# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:42:14 2020

@author: Ana
"""

#Napišite program u kojem se učitava
# prirodan broj, koji se zatim ispisuje u inverznom
# (obrnutom) poretku znamenaka. Ne pretvarati početni broj u string.
#Koristite funkciju „Obrni” koja prima jedan broj i v
#raća broj u inverznom poretku.

#54321
#12345

#5 ??? => 10000 

def brojZn(broj):
    return len(str(broj))
    

def obrni(broj):
    reverse = 0
    while broj > 0:
        znamenka = broj % 10
        reverse = reverse * 10 + znamenka
        broj = broj //10
    print(reverse)
    
broj = int(input("Unesite broj:"))
obrni(broj)
obrni2(broj)
