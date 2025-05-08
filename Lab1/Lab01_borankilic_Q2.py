# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 09:15:19 2021

@author: User
"""

a = int(input('Enter first integer: '))
b = int(input('Enter second integer: '))
c = int(input('Enter third integer: '))

n = 0

if a%2 == 1:
    n += 1
    
if b%2 == 1:
   n += 1
    
if c%2 == 1:
    n += 1
    
print()
print(n,'of the 3 numbers are odd.')