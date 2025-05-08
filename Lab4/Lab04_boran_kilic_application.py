# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 08:35:55 2021

@author: User
"""

import Lab04_boran_kılıç_module

x = True
while x:
    Lab04_boran_kılıç_module.extract_data("ist_data.txt", "ist_districts.txt", "ist_income.txt")
    keyword = input("Enter district to search(quit to exit): ")
    if keyword == "quit":
        x = False
        print("Thank you - Goodbye")
    else:
        income = Lab04_boran_kılıç_module.find_income(keyword, "ist_income.txt")
        if income == 0:
            print(keyword, "not found...")
        else:
            print("Annual Income for ", keyword, ":", str(income))
            