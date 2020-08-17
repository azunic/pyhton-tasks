# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:59:15 2020

@author: Ana
"""
#£Napišite program u kojem korisnik unosi troznamenkasti broj, a
# program ispisuje je li suma znamenki paran ili neparan broj. 
#Koristiti funkciju „SumaZnamenki” koja prima broj i vraća njegovu sumu znamenki. 




def SumaZnamenki(broj):
    
    suma = 0
    while broj > 0:
        suma += broj % 10
        broj/= 10
        broj = int(broj)
    return (suma)
        



broj = int(input("Unesite broj: "))
while (broj <99 or broj > 999):
    broj = int(input("Unesite broj"))
    
print(SumaZnamenki(broj))
if(SumaZnamenki(broj) % 2 == 0):
    print("Parna je")
else:
    print("neparna je")