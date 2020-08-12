# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:27:01 2020

@author: Ana
"""

#Napišite program u kojem korisnik ponavlja unos dok
# god ne pogodi tajnu šifru koja je zapisana u programu.  



lozinka = "Ana12345"

x = input("Unesite sifru: ")

while (lozinka !=x):
    x=input("Unesite ponovno")



print("Pogodili ste svaka cast")