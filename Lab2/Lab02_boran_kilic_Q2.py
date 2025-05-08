# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:50:48 2021

@author: User
"""

a = int(input("enter first int > 0 [0 to quit]: "))
while a<0:
    print("You must enter a positive int, try again....")
    a = int(input("enter first int > 0 [0 to quit]: "))
if a!=0:
    b = int(input("enter second int > 0 [0 to quit]: "))    
    while b<0:
        print("You must enter a positive int, try again....")
        b = int(input("enter second int > 0 [0 to quit]: "))
    if b!=0:
        if a < b:
            Range = range(a,b+1)
        else:
            Range = range(b,a+1) 

        for i in Range:
            total=0
            s = str(i)
            for ch in range(0,len(s)):
                total += int(s[ch])**len(s)
            if total == i:
                print(i,"is a pretty number")
                