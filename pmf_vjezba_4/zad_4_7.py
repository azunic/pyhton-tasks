# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:25:58 2020

@author: Ana
"""

#Napišite program koji će za dva unesena broja i opera
#ciju (+, -, * ili /) izračunati njihov zbroj, razliku, 
#umnožak ili kvocijent. Ukoliko je drugi broj nula, 
#ne računati kvocijent, nego ispisati poruku „Dijeljenje s 
#nulom“. Ukoliko je operacija pogrešno unesena, ispisati por
#uku „Niste dobro unijeli operaciju!”.

A = int(input("Unesite broj"))
B = int(input("Unesite broj b"))
operacija = input("Unesite racunsku operaciju")

if (operacija == "+"):
    zbroj = A + B
    print(zbroj)
elif (operacija == "-"):
    oduzimanje = A - B
    print(oduzimanje)
elif (operacija == "*"):
    mnozenje = A * B
    print(mnozenje)
elif (operacija == "/"):
    if (B == 0):
        print ("Dijeljenje s nulom")
    else:
        djeljenje = A / B
        print(djeljenje)
else:
    print("Niste dobro unijeli operaciju")
