# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 01:15:22 2020

@author: uzumakinagato
"""


N = int(input())

'''
for i in range(1,N+1):
    if N%i == 0:
        print(int(N/i))
'''
i = 1
while i <= N:
    if N%i == 0:
        print(int(N/i))
    i +=1
    