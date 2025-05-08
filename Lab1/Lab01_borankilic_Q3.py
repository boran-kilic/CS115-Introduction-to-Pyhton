# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 09:13:30 2021

@author: User
"""

a = int(input('Enter starting hour: '))
b = int(input('Enter starting minute: '))
c = int(input('Enter ending hour: '))
d = int(input('Enter ending minute: '))
print()
#total minutes of starting
ms = a*60 + b
#total minutes of ending
me = c*60 + d
#total minutes of work
mw = me - ms

if mw <= 0:
    print('Starting time must be before ending time...') 
elif mw < 35:
    print('Not enough time for lunch :(')
else:
    print('You can have lunch!')
    
    
