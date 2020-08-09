# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:09:25 2020

@author: Ana
"""

#Napišite program koji učitava podatke godi
#ne, visina i težina. Nakon što unesete podatke,
# ukoliko imate više od 18 godina, program će izračunati
# vašu idealnu tjelesnu masu (BMI=težina/visina**2). Na 
#ekranu će vam se ispisati vaš BMI, te kategorija u koju pripadate.

broj_godina = int(input("Unesite vas broj godina: "))

if (broj_godina > 18):
    visina = int(input("Unesite vasu visinu: "))
    tezina = int(input("Unesite vasu tezinu: "))
    bmi = tezina / (visina*visina)
    print(round(bmi*1000, 2))
    
    if(bmi < 18.5):
        print("Mrsavost")
    elif(bmi < 25):
        print("Normalna tezina")
    elif (bmi < 30):
        print("prekomjerna tezina")
    elif(bmi >= 30):
        print("Pretilost")
else:
    print("Nemate 18 godina!")
