# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

N = int(input())

def gunung(x):
    if x==1:
        print('*')
    else:
        gunung(x-1)
        print('*'*x)
        gunung(x-1)

gunung(N)
