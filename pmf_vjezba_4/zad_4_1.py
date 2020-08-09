# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 23:07:52 2020

@author: Ana
"""

# "Napišite program u koj
# "em korisnik unosi radijus kruga. Ukoliko je
# "radijus manji od nula ispisati poruku „Krug ne postoji.“, u
# "koliko je radijus jednak nula ispisati „Krug je točka.“, a
# " inače izračunati i ispisati površinu kruga zaokruženu na 3 decimale.


import math

radijus = int(input("Unesite radijus kruga: "))

if (radijus < 0):
    print("Krug ne postoji")
elif (radijus == 0):
    print("Krug je tocka")
else:
    povrsina = 2 * radijus * math.pi
    print(povrsina)
