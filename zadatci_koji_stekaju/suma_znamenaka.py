# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:04:43 2020

@author: Ana
"""


#Napišite program u kojem korisnik unosi broj, 
#a program ispisuje je li suma znamenki paran ili neparan broj. 
##Koristiti funkciju „SumaZnamenki” koja prima
# broj i vraća njegovu sumu znamenki. 

def SumaZnamenki(broj):
    
    suma = 0
    
    while broj > 0:
        suma += broj % 10 
        broj  =broj // 10
    print(suma)
    
    if (suma % 2 ==0):
        print("paran")
    else:
        print("Neparan")
    
    
 
    
    
broj = int(input("Unesite broj po zelji: "))

SumaZnamenki(broj)