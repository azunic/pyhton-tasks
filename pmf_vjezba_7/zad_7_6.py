# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 00:09:58 2020

@author: Ana
"""

#Napišite program koji učitava riječ i ispisuje broj samoglasnika

string = input("Unesite rijec:")

suma = 0
samoglasnici = "aeiou"

for j in range(len(string)):
    if (string[j] =="a" or string[j]=="e" or string[j]=="i" or string[j]=="o" or string[j] =="u"):
        suma +=1    
print(suma)