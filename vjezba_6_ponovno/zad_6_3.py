# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:20:32 2020

@author: Ana
"""

#apišite program koji će tražiti od
# korisnika da ponavlja unos dok god ne unese
# četveroznamenkasti broj. Program na kraju ispisuje broj 
#kojega je korisnik unio.
#Koristite funkciju „Unos” koja ne prima parametre i vraća vrijednost.

def Unos():
    
    broj = int(input("Unesite cetveroznamenkasti broj: "))
    
    while(broj < 999 or broj > 9999):
        broj = int(input("Unesite broj koji je cetveroznamenkast: "))
    return(broj)


print(Unos())