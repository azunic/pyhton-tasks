# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:10:57 2020

@author: Ana
"""

#Napišite program koji učitava riječ i ispisuje novu
# riječ dobivenu tako da se iz unesene riječi izbriše svaki treći znak.


string = "anakonda"
         #1 2 3 4 5 6 7 8 


novarijec = ''
for j in range(0,len(string)):
    if (j % 3 == 0):
        continue
    else:
        novarijec += string[j]
        
print(novarijec)
        
