# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 04:09:56 2020

@author: uzumakinagato
"""


def digitsum(power): 
    return sum([int(i) for i in str(pow(2, power))]) 
      

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(digitsum(n)) 
    
    