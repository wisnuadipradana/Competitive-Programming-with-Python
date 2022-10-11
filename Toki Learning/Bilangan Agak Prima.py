# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 00:21:07 2020

@author: uzumakinagato
"""


N = int(input())

for j in range(N):
    x = int(input()) 
    n = 0
    for i in range(2,int(x**.5)+1):
        if x%i == 0:
            n += 1 
    if n in range(2):
        print('YA') 
    else:
        print('BUKAN')