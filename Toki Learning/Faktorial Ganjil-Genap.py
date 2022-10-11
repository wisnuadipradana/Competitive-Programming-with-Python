# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

N = int(input())

def f(x):
    if x>1:
        if x%2==0:
            return x*f(x-1)//2
        else:
            return x*f(x-1)
    elif x==1:
        return 1

print(f(N))