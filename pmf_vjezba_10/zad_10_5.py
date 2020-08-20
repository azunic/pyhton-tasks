# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:14:32 2020

@author: Ana
"""

#Napišite program u kojem korisnik unosi 
#10 pozitivnih četveroznamenkastih brojeva u n
#iz Brojevi (provjeravati korisnikov unos svaki
# put i osigurati da su u niz uneseni samo ispravni brojevi).
#	Proste brojeve iz niza Brojevi smjestiti u 
#niz Prosti, a 	druge brojeve smjestit u niz NisuProsti.
#	Ispisati niz Prosti i NisuProsti.
brojeviniz = []
i = 0
n = 5
prost = []
nisuprosti = []

def prostbroj(x):
    
    for i in range(2,x):
        if (x % i ==0):
            return False
        else:
            return True
     
while (i < n):
    broj = int(input("Unesite broj: "))
    while ( broj < 999 or broj > 9999):
        broj = int(input("Unesite broj: "))
    brojeviniz.append(broj)
    i+=1
    
for x in range(0,len(brojeviniz)):
        if(prostbroj(x)):
           print(prostbroj(x))
            
    
        

print(prost)
print(nisuprosti)
            