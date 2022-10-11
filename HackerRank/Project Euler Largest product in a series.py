# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:18:54 2020

@author: uzumakinagato
"""


import sys

def product(x,k):
    prod = 1 
    for i in range(k):
        prod *= int(x[i]) 
    return prod 

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')  
    n,k = [int(n),int(k)]
    num = input().strip()
    list = []  
    for i in range(n-k+1):
        x = num[i:k+i]  
        list.append(x) 
    print(list)
    prod = [] 
    for j in range(n-k+1):
        prod.append(product(list[j],k))
    print(prod)
    print(max(prod)) 
        

