# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 09:05:47 2021

@author: User
"""

from Personnel import*

def read_file(filename):
    file = open(filename, 'r')
    lst = []
    for line in file:
        line = line.strip()
        data = line.split(',')
        id = int(data[0])
        name = data[1]
        department = data[2]
        status = data[3]
        salary = float(data[4])
        personnel = Personnel(id,name,department,status,salary)
        lst.append(personnel)
    return lst

p_list = read_file('personnel.txt')
d = {}
for i in range(len(p_list)):
    p_list[i].increase_salary()
    if p_list[i].get_status()=='B':
        d[p_list[i].get_id()] = p_list[i]
        
        
print('All personnel:\n',p_list)
print('Personnel With Both Managerial and Academic Responsibilities:')
print(d)
