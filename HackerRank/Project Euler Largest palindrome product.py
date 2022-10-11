# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 01:28:35 2020

@author: uzumakinagato
"""

import sys

'''
def isprime(x): 
    if x == 1:
        return False
    else:  
        prim = 0
        for i in range(2,int(x**.5)+1):
            if x%i == 0:
                prim += 1
        if prim == 0:
            return True
        else:
            return False   
'''

def digit3(x):
    for k in range(100,1000,1):
        if x%k == 0 and len(str(int(x/k))) == 3 :
            return True
        else :
            return False

def palindrome6(x):
    a = x//100000
    b = (x//10000)%10
    c = (x//1000)%10  
    if x%1000 == 100*c+10*b+a :
        return True
    else :
        return False 

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = 0 
    for j in range(n,101100,-1):
       if digit3(j) == True and palindrome6(j) == True :
           print(j)
           

''' 
hasil = []
for i in range(t):
    for j in range(list[i],101100,-1):
        for k in range(100,1000,1):
            for l in range(100,1000,1):
                if k*l == j and palindrome6(j) == True :
                    hasil.append(j)
                    break
'''



