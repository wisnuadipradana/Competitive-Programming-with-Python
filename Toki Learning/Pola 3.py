# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 21:02:12 2020

@author: uzumakinagato
"""


N = int(input())
sum = 0

for i in range(1,N+1):
    for j in range(1,i): 
        sum += 1
        print(sum%10, end="")
    if i==1:
        print("0") 
    else:
        print((sum+1)%10) 
        sum += 1
 
    