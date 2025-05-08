# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 08:48:35 2021

@author: User
"""

def extract_data(data_file, districts_file, output_file):
    """
    Creates a file includes annual income for districts
    
    Parameters:
    data_file (file): data of districts
    districts_file (file): names of districts
    output_file (file): result
    """
    data = open(data_file, "r")
    districts = open(districts_file, "r")
    output = open(output_file, "w")
    
    data_list = data.readlines()
    district_list = districts.readlines()
    
    for i in range(len(data_list)):
        dist_name = district_list[i][:-1]
        income = ""
        for i in data_list[i][-4::-1]:
            if i == "(":
                break
            else:
                income += i
        
        income = income[::-1]
        output.write(dist_name + "\t" + income + "\n")
    data.close()
    districts.close()
    output.close()


def find_income(dist_name, file_name):
    """
    finds annual income for given district
    
    Parameters:
    dist_name (str): input from user
    file_name (file): the file contains data
    
    Returns:
    str: annual income
    """
    file = open(file_name, "r")
    for word in file.readlines():
        if dist_name.lower() in word.lower():
            income = ""
            for i in word[-2::-1]:
                if i == "\t":
                    return "$"+income[::-1]+".00"
                else:
                    income += i
    return 0.0
