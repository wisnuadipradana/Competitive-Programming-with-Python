# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 01:44:08 2020

@author: uzumakinagato
"""

import sys

def Collatzline(x):
    n = 1
    while x != 1:
        if x%2 == 0:
            x = x//2
            n += 1
        else :
            x = 3*x+1
            n += 1
    return n 

arr = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(1,n+1):
        arr.append([Collatzline(i),i]) 
    list = max(arr)
    print(list[1])  

