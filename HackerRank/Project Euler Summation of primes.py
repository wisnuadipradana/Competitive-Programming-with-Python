# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:39:52 2020

@author: uzumakinagato
"""


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
    list.append(0) 
    while list[-1] <= n: 
        if primeornot(i)  == True:
            list.append(i) 
        i += 1 
    list.remove(list[-1])   
    sum = 0
    for i in list:
        sum += i
    print(sum) 
