# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:45:31 2020

@author: uzumakinagato
"""


N = int(input())

for i in range(1,N+1):
    if i%10 == 0:
        continue
    elif i==42:
        print("ERROR")
        break
    else :
        print(i) 