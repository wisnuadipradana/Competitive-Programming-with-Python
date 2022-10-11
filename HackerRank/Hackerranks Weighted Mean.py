# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 17:55:04 2020

@author: uzumakinagato
"""

t = int(input().strip())
m = list(map(int, input().strip().split(' ')))  
n = list(map(int, input().strip().split(' ')))  

kali = []
for i in range(t):
    kali.append(m[i]*n[i]) 

print(round(sum(kali)/sum(n) ,1))
 