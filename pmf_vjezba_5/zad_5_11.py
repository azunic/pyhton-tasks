# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 18:13:47 2020

@author: Ana
"""

#Napišite program u kojem korisnik učitava cij
#ele brojeve u intervalu od 1 do 999 uključivo.
#Učitavanje i kraj programa se izvršava kada korisnik unese 0.

#Ispisati broj unesenih jednoznamenkastih, dvoznamenkastih i t
#roznamenkastih brojeva.

broj=int(input("Unesite broj"))
    
brojac_jednoznamenkastih = 0
brojac_dvoznamenkastih = 0
brojac_troznameknastih = 0

while (broj !=0)
    
      broj=int(input("Unesite broj")) 
      if (broj > 0 and broj < 10 ):
          brojac_jednoznamenkastih += 1
      elif(broj >= 10 and broj <= 99):
           brojac_dvoznamenkastih += 1
      elif (broj >= 100 and broj <= 999):
          brojac_troznameknastih += 1
      print(brojac_jednoznamenkastih,brojac_dvoznamenkastih,brojac_troznameknastih)
        
        
