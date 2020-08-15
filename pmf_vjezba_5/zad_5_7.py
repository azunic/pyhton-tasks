# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 17:33:14 2020

@author: Ana
"""

#Napisati program koji će ispisati sve troznamenkaste brojeve
# koji su djeljivi s 3.
#Riješiti zadatak korištenjem i while i for petlje.


#najmanji broj troznamnekasti je 100 a najveci 999

for i in range(100,999):
    if i %  3 == 0:
        print(i)
        
broj = 100
while (broj <= 999):
    if broj %  3 == 0:
    	print(broj)
    broj += 1
    
