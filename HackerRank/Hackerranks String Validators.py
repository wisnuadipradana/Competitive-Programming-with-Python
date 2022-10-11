# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:56:35 2020

@author: uzumakinagato
"""

if __name__ == '__main__':
    s = input()

a = [i for i in s if i.isalnum() == True] 
if len(a) != 0:
    print('True')
else :
    print('False')

b = [i for i in s if i.isalpha() == True] 
if len(b) != 0:
    print('True')
else :
    print('False')

c = [i for i in s if i.isdigit() == True] 
if len(c) != 0:
    print('True')
else :
    print('False')

d = [i for i in s if i.islower() == True] 
if len(d) != 0:
    print('True')
else :
    print('False')

e = [i for i in s if i.isupper() == True] 
if len(e) != 0:
    print('True')
else :
    print('False')