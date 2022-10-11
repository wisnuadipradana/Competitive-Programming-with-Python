# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:58:11 2020

@author: uzumakinagato
"""

def sumdivisor(x):
    sum = 0
    for i in range(1,x):
        if x%i == 0:
            sum += i
    return sum 

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    list = []; jumlah = 0
    for i in range(1,n):
        p = sumdivisor(i) 
        if sumdivisor(p) == i and i != p and i<p:
            jumlah += i+p
    print(jumlah)

    

