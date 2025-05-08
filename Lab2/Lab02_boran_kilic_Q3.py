# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:40:46 2021

@author: User
"""

string = input("Enter a string (empty to quit): ")
while string:
    reverse = string [::-1]
    if string == reverse:
        print("It is a mirror string")
    else:
        print("It is NOT a mirror string")
    string = input("Enter a string (empty to quit): ")   
if string == "":
    print("bye!")
    