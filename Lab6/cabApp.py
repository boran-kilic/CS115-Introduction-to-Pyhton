# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:01:55 2021

@author: User
"""

from cab import *

def find_equal(lst, cab1):
    """
    

    Parameters
    ----------
    lst : list of cabs
        
    cab1 : the cab object that contains the km and type that we are 
    searching in our list
    
        

    Returns the number of cabs that has the qualifications
    that we want
    -------
    count : integer
        

    """
    
    count = 0
    for cab in lst:
        
        if cab == cab1:
            count += 1
           
    return count   

def readfile(fileName):
    """
    

    Parameters
    ----------
    fileName : file
        The file that contains the cab types and kms

    Returns a list of cabs, with their km
    -------
    lst : list of cab objects
        

    """
    lst = []
    file = open(fileName , 'r')
    for line in file:
        
        line = line.strip()
        line = line.split(':')
        type_of_cab = line[0]
        km = int(line[1])
        if type_of_cab == 'Sedan':
            car = Sedan(type_of_cab , km)
        elif type_of_cab == 'Hatchback':
            car = Hatchback(type_of_cab , km)    
        lst.append(car)
    file.close()
    return lst    
   
    
list_of_cabs = readfile('cabs.txt')   
lst_sedan = []
lst_hatchback = []
for car in list_of_cabs :
    if car.get_typeOfCab() == 'Sedan':
        lst_sedan.append(car.get_kms())
    else:
        lst_hatchback.append(car.get_kms())
sedan_km = sum(lst_sedan)    
hatchback_km = sum(lst_hatchback)        
   
        
total_km = sedan_km + hatchback_km
print('---Kilometers driven for each cab---')
print('Hatchback : ' , hatchback_km,' kilometers')
print('Sedan : ' , sedan_km,' kilometers')
print()
print('Total number of kilometers driven by all Cabs : ', total_km)

fare_s = 0
fare_h = 0
for car in list_of_cabs:
    if car.get_typeOfCab() == 'Sedan':
        s = Sedan.calculate_fare(car)
        fare_s += s
    if car.get_typeOfCab() == 'Hatchback':
        h = Hatchback.calculate_fare(car)
        fare_h += h 
fare = fare_s + fare_h

print('Total fare earned from all cabs (in dolars) : ' , fare)
print()
print('Sorted Cabs:')
list_of_cabs.sort()
print(list_of_cabs)

cab2 = Cab('Sedan' , 200) 
num = find_equal(list_of_cabs, cab2 )
print(f'There are {num} Sedan cabs with 200 kms.')
    









