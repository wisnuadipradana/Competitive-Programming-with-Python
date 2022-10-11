# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:52:16 2020

@author: uzumakinagato
"""


N = int(input())

for j in range(N):
    x = int(input())
    if x ==1:
        print('BUKAN')
    else: 
        n = 0
        for i in range(2,int(x**.5)+1):
            if x%i == 0:
                n += 1
        if n==0:
            print('YA')
        else:
            print('BUKAN')