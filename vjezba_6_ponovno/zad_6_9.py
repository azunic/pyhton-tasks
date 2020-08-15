# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:20:26 2020

@author: Ana
"""

#"#Napišite program u kojem korisnik unosi 8 riječi. 
#"Ispisati najdulju riječ i od koliko znakova se sastoji.
lista_svih_rijeci = []
najdulja_rijec = ''


for i in range(8):
    rijec = input("Unesite string")

   
    duljina1 = (len(najdulja_rijec))
    duljina2 = (len(rijec))

    if (duljina2 > duljina1):
        najdulja_rijec = rijec




duljina_najdulje_rijeci=len(najdulja_rijec)




print(najdulja_rijec)
print(duljina_najdulje_rijeci)
    
    