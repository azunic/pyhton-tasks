# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:25:45 2020

@author: Ana
"""

#Napišite program u kojem se učitava čet
#veroznamenkasti prirodan broj. Program treb
#a ispisati je li zbroj prve i četvrte znamenke
# paran. Korisnik mora ponavljati unos dok ne unese četveroznamenkasti broj. 
#Koristite funkcije: 
#„Znamenkast” koja prima broj i vraća vrijednost 
#„jednoznamenkast” ili „dvoznamenkast” kao rezultat.
#„ZbrojZnam” koja prima broj i vraća zbroj prve i
# četvrte znamenke kao rezultat. 
        
    
def zbrojznam(broj):
      suma = 0
      prva_znamenka = broj //1000
      zadnja_znamenka = broj % 10
      suma = prva_znamenka + zadnja_znamenka
      if(suma % 2 == 0):
          return(suma)
      
        
def znamenkast(suma):
    
    if(suma > 1 and suma < 9):
        print("Jednoznamenkast")
    elif( suma > 9 and suma <99 ):
        print("dvoznamenkast")
    
      



broj = int(input("Unesite broj: "))
while( broj < 999 or broj > 9999):
        broj = int(input("Unesite broj: "))
print(znamenkast(broj))
print(zbrojznam(broj))
