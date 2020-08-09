# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 14:24:33 2020

@author: Ana
"""

#Napišite program koji će učitati dvije točke u trodim
#enzionalnom prostoru A=(x1,y1,z1) i B=(x2,y2,z2).
# Ispišite koliki je kvadrat udaljenosti između točaka A i B.

	#Izračun kvadrata udaljenosti:
	#d2=(x2-x1) 2+(y2-y1) 2+(z2-z1) 

x1, y1, z1 = list(map(int, input("Unesite x1 y1 z1 za prvu tocku ").split()))
x2, y2, z2 = list(map(int, input("Unesite x2 y2 z2 za drugu tocku ").split()))
#"5 3 4"
#["5", "3", "4"]
#[5, 3, 4] 

izraz = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2

print("kvadrat udaljenosti iznosi: ", izraz)