# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:32:24 2020

@author: uzumakinagato
"""

N = int(input())
total = 0
arr = map(int, input().split()) 
listarr = list(arr)

if len(listarr) == N:
    for i in range(N):
        total += listarr[i]
    print(total)  

