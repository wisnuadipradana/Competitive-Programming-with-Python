# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 00:21:53 2020

@author: uzumakinagato
"""


import sys

sum = 0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())  
    sum += n
sum = str(sum)
print(int(sum[0:10]))  
   
    