# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:36:51 2021

@author: User
"""

import random
total = 0
count = 0
while total < 1001 and count < 101:
    random_number = random.randint(1,20)
    total += random_number
    count += 1
    
print ("Sum of",count, "random ints in [1..20] is", total)
