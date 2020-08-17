# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:51:09 2020

@author: Ana
"""

#Napišite program koji učitava riječ i 
#ispisuje novu riječ dobivenu tako da se iz unesene r
#iječi izbriše svaki treći znak.

string = "majmun"

#treba izbacit svako treci znak majmun
                               # 123456 triba izbacit j i n
for i in range(1,len(string),3):
    print(string[i])
    print(string)