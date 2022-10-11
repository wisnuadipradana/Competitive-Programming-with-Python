# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 20:23:49 2020

@author: uzumakinagato
"""

def divisor(x):
    sum = 0
    for i in range(1,x+1):
        if x%i == 0:
           sum += 1
    return sum

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 1
    while divisor((i*(i+1))//2) <= n:
        i += 1
    print((i*(i+1))//2)



