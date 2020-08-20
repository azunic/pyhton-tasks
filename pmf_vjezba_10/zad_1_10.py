# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:11:00 2020

@author: Ana
"""

#Napišite program koji će za uneseni string
# ispisati je li palindrom (čita li se jednako sprijeda i straga, npr. rotor).

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")
      
      