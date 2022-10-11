# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:25:37 2020

@author: uzumakinagato
"""


N = int(input())

for i in range(1,N+1):
    for j in range(N-i,0,-1):
        print(" ", end="")
    print(i*'*') 
