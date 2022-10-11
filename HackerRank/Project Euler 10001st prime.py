# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 03:15:18 2020

@author: uzumakinagato
"""


import sys

def primeornot(x):
    N = 0
    for i in range(2,int(x**.5)+1):
        if x%i == 0:
            N += 1
    if x==1:
        return False 
    if N==0 : 
        return True
    else :
        return False

    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 1; list = []
    while True: 
        i +=1
        if primeornot(i)  == True:
            list.append(i)  
            if len(list) == n:
                print(list[-1])
                break 
    