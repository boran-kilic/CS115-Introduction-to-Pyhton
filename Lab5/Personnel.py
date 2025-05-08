# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 08:48:57 2021

@author: User
"""

class Personnel():
    def __init__(self,id,name,department,status,salary):
        self.__id = int(id)
        self.__name = name
        self.__department = department
        self.__status = status
        self.__salary = salary
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_department(self):
        return self.__department
    
    def get_status(self):
        return self.__status
    
    def get_salary(self):
        return self.__salary
    
    def increase_salary(self):
        if self.__status == 'M':
            self.__salary = self.__salary*112/100
        if self.__status == 'A':
            self.__salary = self.__salary*115/100 
        if self.__status == 'B':
            self.__salary = self.__salary*118/100 
        
    def __repr__(self):
         s ='Id: '+str(self.__id)+'\nName: '+ self.__name +'\nDepartment: '+self.__department + '\nStatus: ' + self.__status + '\nSalary: '+str(self.__salary)+ ' TL\n'
         return s
    
    def __str__(self):
         s ='Id: '+str(self.__id)+'\nName: '+ self.__name +'\nDepartment: '+self.__department + '\nStatus: ' + self.__status + '\nSalary: '+str(self.__salary)+ ' TL\n'
         return s