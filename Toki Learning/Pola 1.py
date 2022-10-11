# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 17:43:05 2020

@author: uzumakinagato
"""

N,k = input().split() 
N = int(N); k = int(k)

for i in range(1,N):
    if i%k != 0:
        print(i, end=" ") 
    else :
        print("*", end=" ")

if N%k == 0:
    print("*")
else :
    print(N)