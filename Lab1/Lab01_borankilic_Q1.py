# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 08:42:33 2021

@author: User
"""

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
x = float(input('Enter x: '))

result = a*x**2 + b*x + c
print()
print('f(x) =',a,'* x ** 2 +',b,'* x +', c)
print('f(',x,')= ' + f'{result:.2f}')