# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 08:31:46 2021

@author: User
"""

def is_spaced(password): 
   """
   If space between all digits is not same
   
   Parameters:
   password (str): password
   
   Returns:
   bool: result
   """
   
   difference1 = ord(password[1]) - ord(password[0])
   for c in range(0,len(password)-1):
       difference2 = ord(password[c+1]) - ord(password[c])
       if abs(difference1) != abs(difference2):
           result = True
           break 
       else:
           result = False
   return result      


def contains_birthyear(password,birth_year):
    """
    If the password contains birth year
    
    Parameters:
    password (str): password
    birt_year (str): year of birth
    
    Returns:
    bool: result
    """
    digit = 0
    while password:
        if digit == len(birth_year):
            break
        if birth_year[digit] == password[0]:
            result = True
            digit += 1
        else:
            result = False
        password = password[1:]
    return result


def is_valid_password(password, birt_year):
    """
    If the password is valid
    
    Parameters:
    password (str): password
    birt_year (str): year of birth
    
    Returns:
    bool: result
    """
    if len(password)<3 or is_spaced(password) == False or contains_birthyear(password,birth_year):
        result = False
    else:  
        result = True
    for i in range(0,len(password)):
        if ord(password[i]) not in range(ord("0"),ord("9")+1):
            result = False
            break
    return result


password = input("Enter a password: ")
birth_year = input("Enter year of birth: ")

while is_valid_password(password, birth_year) == False:
    print(password, "is not a valid password - try again")
    password = input("Enter a password: ")
    birth_year = input("Enter year of birth: ")

print("Thank you - password is valid")