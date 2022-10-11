# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

n = list(map(int, input().split()))

def f(x, k):
    if k==0:
        return x
    else:
        return abs(n[0]*f(x, k-1)+n[1])

print(f(n[3], n[2])) 