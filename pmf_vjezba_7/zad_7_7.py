# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 00:19:48 2020

@author: Ana
"""

#Napišite program u kojem korisnik unos
#i jedan prirodan broj. Program treba provjeriti je li uneseni bro
#j palindrom. Tj. piše li se jednako s lijeve i s desne strane.
# Ne pretvarati početni broj u string.
#oristite funkciju „Obrni” koja prima jedan broj kao argument i
# vraća jedan broj kao rezultat.



N = int(input('Unesi prirodni broj N>= 10: '))
palindrom = 0
pom = N
while pom > 0:
    palindrom = palindrom * 10 + pom % 10
    pom = pom // 10
if palindrom == N:
    print('Broj', N, 'je palindrom')
else:
    print('Broj', N, 'nije palindrom')