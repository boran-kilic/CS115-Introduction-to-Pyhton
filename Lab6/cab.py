# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:01:54 2021

@author: User
"""

class Cab:
    
    def __init__(self, typeOfCab, kms):
        self.__typeOfCab = typeOfCab
        self.__kms = kms
      
    def get_kms(self):
        return int(self.__kms)
    
    def get_typeOfCab(self):
        return self.__typeOfCab
        
    def __lt__(self, other)    :
        return self.__kms < other.__kms
        
        
        
    def __eq__(self, other)   :
        if self.__kms == other.get_kms() and self.__typeOfCab == other.__typeOfCab:
            return True
        else:
            return False
        
    def __repr__(self):
        
        return self.__typeOfCab+' '+str(self.__kms) + '\n'
        

class Sedan(Cab):
    __price_per_km = 2
    def __init__(self, typeOfCabs, kms):
        Cab.__init__(self, typeOfCabs, kms)
              
        
    def calculate_fare(self) :
        fare = Sedan.__price_per_km * self.get_kms()
        return fare 
        
class Hatchback(Cab):      
    __price_per_km = 1.5
    def __init__(self, typeOfCabs, kms):
        Cab.__init__(self, typeOfCabs, kms)
              
        
    def calculate_fare(self) :
        fare = Hatchback.__price_per_km * self.get_kms()
        return fare 
        