# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 23:30:16 2020

@author: Ana
"""

#Natjecanje u videoigri se sastoji od 4 l
#ige u koje su igrači raspoređeni na tem
#elju osvojenog broja bodova. Za uneseni 
#broj bodova potrebno je ispisati u koju ligu ig
#rač spada. U slučaju pogrešnog potrebno je ispi
#sati poruku o pogrešci. Bodovi mogu biti realni brojevi. 
#Lige su:
#	D – bodovi [0 – 25>
#	C – bodovi [25 – 50>
#	B – bodovi [50 – 75>
#	A – bodovi [75 – 100]

broj_bodova = int(input("Unesite broj bodova: "))

if (broj_bodova > 0 and broj_bodova < 25 ):
    print ("D")
elif (broj_bodova >= 25 and broj_bodova < 50):
    print("C")
elif (broj_bodova >= 50 and broj_bodova < 75):
    print("B")
elif (broj_bodova >= 75 and broj_bodova <= 100):
    print("A")
else:
    print("Pogresno unesen broj bodova")
