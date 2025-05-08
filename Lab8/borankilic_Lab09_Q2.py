# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:21:11 2021

@author: User
"""

import numpy as np

covid_data = np.loadtxt("covid_data.txt ")
covid_country = np.loadtxt("covid_country.txt", dtype='str', skiprows= 1)
covid_data = covid_data.transpose()

av = np.mean(covid_data[:,0]) 
print(f'Average cases per 1 million: {av:.1f}' )

print('Countries in Europe',covid_country[covid_country[:,1] == 'Europe'][:,0])


case = covid_data[:,0]
print('Average cases per 1 million: ' , case)

print('Countries with over 10000 cases per 1 million:\n',covid_country[covid_data[:,0] > 10000][:,0])

asia = covid_data[covid_country[:,1] == 'Asia']
max_asia = np.max(asia[:,1])
print('Maximum deaths per 1 million in Asia: ',max_asia)

max_country = covid_country[ (covid_data[:,1] == max_asia) & (covid_country[:,1] == 'Asia')][:,0]
print('Country with maximum deaths per 1 million in Asia: ', max_country)

test_country = (np.array([covid_country[:,0], covid_data[:,2]])).transpose()
np.savetxt('test_data.txt',test_country,fmt='%s')

print(test_country)
