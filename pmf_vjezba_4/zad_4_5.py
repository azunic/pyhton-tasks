# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 23:54:05 2020

@author: Ana
"""

#S tipkovnice se unose 3 jednoznamenkasta broja
# A, B i C. Potrebno je između operatora ‘+’ i ‘*’ o
#dabrati operator koji se može primijeniti na unesene 
#brojeve kako bi se dobio ispravan matematički izraz.
#Na izlazu se ispisuje poruka ‘+=‘ ili ‘
#*=‘ ili ‘Hokus Pokus’ u slučaju da izraz nije moguće složiti.
	
#graničenje ulaza: A, B i C su tri jednozna
#menkasta broja (0, pozitivni i negativni bro
#jevi) koji se unose s tipkovnice.

#U ovom zadatku pokazano je kako ulazne vrijednos
#ti mogu uključivati određena ograničenja, koja se 
#po unosu vrijednosti odmah moraju provjeriti!

A = 10
B = 10
C = 10

while (A >= 10):
    A = int(input("Unesite prvi jednoznamenkasti broj: "))
    
while (B >= 10):
    B = int(input("Unesite drugi jednoznamenkasti broj: "))
    
while (C >= 10):
    C = int(input("Unesite treci jednoznamenkasti broj: "))

if (A + B == C):
    print("+=")
elif (A * B == C):
    print("*=")
elif (A + B != C):
    print("Hokus pokus")