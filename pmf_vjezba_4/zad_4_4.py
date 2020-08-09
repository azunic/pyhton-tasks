# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 23:38:20 2020

@author: Ana
"""

#Napišite program koji će od korisnika zatražiti  u
#nos tri stringa. Provjeriti jesu li stringovi uneseni 
#prema abecednom redoslijedu,i ako nisu da ih se poslozi po redoslijedu. 
#na primjer zec pas macka treba ispisat macka pas zec ...
 
string_1 = input("Unesite prvi string")
string_2 = input("Unesite drugi string")
string_3 = input("Unesite treci string")
 
if (string_1 <string_2 < string_3):
     print (string_1, string_2, string_3)
elif(string_1 < string_3 < string_2):
    print(string_1, string_3, string_2)
elif(string_2 < string_1 < string_3):
    print(string_2, string_1, string_3)
elif(string_2 < string_3 < string_1):
    print(string_2, string_3, string_1)
elif(string_3 < string_1 < string_2):
    print(string_3, string_1, string_2)
elif(string_3 < string_2 < string_1):
    print(string_3, string_2, string_1)