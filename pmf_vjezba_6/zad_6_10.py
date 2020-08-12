# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:10:04 2020

@author: Ana
"""

#Napišite program koji učitava tekst i jednu riječ.  
#Odrediti sve pozicije na kojima se u tekstu pojavljuje  unesena riječ. 



tekst= "Nakon bolnog poraza od Španjolske (9-8) u polufinalu Eura bolnog"
rijec = "bolnog"

novi_tekst = tekst.split()
print(novi_tekst)
for  pozicija,i in enumerate(novi_tekst):
    if (i==rijec):
        print (pozicija)



