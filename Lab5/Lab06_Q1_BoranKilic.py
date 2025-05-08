# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 08:32:13 2021

@author: User
"""

list_2d = [['This', 'is', 'lab', 'Script'],
           ['We', 'should', 'finish', 'it'],
           ['we', 'solve', 'some', 'questions']]

def formEqualLength(inList,n):
    """
    forms a sentence from the words with the length n 
    by putting a space between the words

    Parameters
    ----------
    inList : 2D list
        
    n : int
        length of words 

    Returns
    -------
    snt : str
        sentence

    """
    
    snt = ''
    for i in range( len( inList)):
        for w in range( len(inList[i])):
            if len(inList[i][w]) == n:
                if snt == '':
                    snt += inList[i][w]
                else:
                    snt += ' '+ inList[i][w] 
    return snt
print('Two Dimensional List:')
for i in list_2d:
    print(i)
print('sentece: ',formEqualLength(list_2d,6))