# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 09:11:15 2021

@author: User
"""

class Country:
    def __init__(self, cName, continent, life_m, life_f):
        self.__country = cName
        self.__continent = continent
        self.__life_male = life_m
        self.__life_female = life_f     
        
    def getCountry(self):
        return self.__country
        
    def getContinent(self):
        return self.__continent
    
    def getLifeMale(self):
        return self.__life_male

    def getLifeFemale(self):
        return self.__life_female
    
    def calculate_average(self):
        average = ( float( self.__life_male ) + float( self.__life_female ) ) / 2
        return average
           
    def __str__(self):
        s = 'Country:' + self.__country + '\n'
        s += 'Average Life Expectancy: ' + str(self.calculate_average()) + '\n'
        
        return s
        
    def __repr__(self):
        s = 'Country:' + self.__country + '\n'
        s += 'Continent: ' + self.__continent + '\n' 
        s += 'Life Expectancy for Males: ' + str(self.__life_male) + '\n'
        s += 'Life Expectancy for Females: ' + str(self.__life_female) + '\n'
        
        return s
    
    def __eq__(self, other):
        return self.__country == other.__country

def readCountries( c_list, filename ):
    file = open( filename, 'r' )
    for line in file:
        data = line.split( ',' )
        c_list.append( Country( data[ 0 ], data[ 1 ], data[ 2 ], data[ 3 ] ) )
    return c_list        

def selectionSort( c_list ):
    for c in range( len( c_list ) ):
        first = c
        for i in range( first + 1, len( c_list ) ):
            if Country.getContinent( c_list[ i ] ) < Country.getContinent( c_list[ first ] ):
                first = i
            if Country.getContinent( c_list[ i ] ) == Country.getContinent( c_list[ first ] ):
                if Country.getCountry( c_list[ i ] ) < Country.getCountry( c_list[ first ] ):
                    first = i
        ( c_list[ c ], c_list[ first ]) = ( c_list[ first ], c_list[ c ] )
    return c_list

def searchCountries( c_list, continent, index ):
    if index >= 0:
        if continent == Country.getContinent( c_list[ index-1 ] ):
            result = searchCountries( c_list, continent, index-1)
            result.append( c_list[ index-1 ] )
            return result
        else: return searchCountries( c_list, continent, index -1)
    else: return []       
    


Countries = []

readCountries( Countries, 'country.txt' )
continent_input = str( input( 'Enter continent to search: ') )
print( 'List of Countries in', continent_input)
for e in searchCountries( Countries, continent_input, len( Countries ) ):
    print( f'{e}\n')
    
country_name, continent_name, male_expectancy, women_expectancy = input( 'Enter country name, continent, life expectany for Men and life expectany for Women: ' ).split(',')
if Country( country_name, continent_name, male_expectancy, women_expectancy) not in Countries:
        Countries.append( Country( country_name, continent_name, male_expectancy, women_expectancy) )    
        print( 'New Country added\n' )
    
selectionSort( Countries )
print( Countries )