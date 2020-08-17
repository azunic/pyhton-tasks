# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:15:49 2020

@author: Ana
"""
#Napišite program koji učitava riječ i ispisuje nov
#u riječ dobivenu tako da se iz unesene riječi izbriše svaki treći znak.
lista = []

string = "anakonda"
broj = len(string)
print(broj)
a = (string[0:broj:3])

lista.append(a)
print(lista)
