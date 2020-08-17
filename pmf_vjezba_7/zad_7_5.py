# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:16:31 2020

@author: Ana
"""
#Doradite prethodni zadatak na način da se unosi 10 brojeva u z
#adanom ograničenju i za svaki broj se ispisuje je li prost ili nije.

    
def Prost(n):
 for i in range(2,n+1):
     if (n % i ==0):
         return False
     else:
       return  True


n=0
brojac = 0
while(n < 1 or n >100 ):
    for i in range(1,5):
        n = int(input("Unesite broj:"))

print(Prost(n))
if (Prost(n)):
    print("Prost je")
else:
    print("Nije prost")

