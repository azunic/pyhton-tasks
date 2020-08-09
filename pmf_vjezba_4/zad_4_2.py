# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 23:16:03 2020

@author: Ana
"""

#Napišite program koji će za unesenu godinu računati 
#je li godina prijestupna. Prijestupne godine su sve go
#dine djeljive s 4 i ako nisu djeljive sa 100, kojima se 
#dodaju one koju su djeljive sa 400.

godina = int(input("Unesite godinu: "))

if (godina % 4 == 0) and (godina % 100 != 0) or (godina % 400 == 0) :
    print("prijestupna")
else:
    print("nije prijestupna")