# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:43:23 2020

@author: Ana
"""
#
#Napišite program u kojem korisnik unosi rečenicu. Svaku poja
#vu riječi “kupus” treba zamijeniti riječju “kelj”. Is
#pisati novu rečenicu.
#	Napomena: riječ kupus mora biti samostalna riječ




recenica = "Jednog lijepog suncanog dana ana je jela kupus"
rijec = 'kelj'

nova_recenica = recenica.split()
print(nova_recenica)


x = recenica.replace("kupus", "kelj")
print(x)

    

