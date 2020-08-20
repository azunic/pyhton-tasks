# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:25:04 2020

@author: Ana
"""

#Napišite program koji učitava riječ i ispisuje broj samoglasnika.

string = "Anakonda"
brojac = 0
stringnovi = string.lower()
print(stringnovi)


for j in stringnovi:
    print(j)
    if( j =="a" or j == "e"):
        brojac +=1 
    print(brojac)

