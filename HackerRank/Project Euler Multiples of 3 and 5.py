# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 02:57:16 2020

@author: uzumakinagato
"""

'''
import sys

list = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    list.append(n)  
    
def multiple3and5(N):
    arr = []  
    for i in range(1,N):
        if i%3 == 0 or i%5 == 0:
            arr.append(i) 
    sum = 0  
    for j in arr:  
       sum +=  j
    return sum 

for i in range(t):
    print(multiple3and5(list[i]))  

'''
'''
import sys

list = []  
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = []
    for i in range(1,n):
        if i%3 == 0 or i%5 == 0:
            arr.append(i) 
    sum = 0
    for j in arr:   
       sum +=  j
    list.append(sum) 
for i in range(t):
    print(list[i]) 
'''

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = (n-1)//3; j = (n-1)//5; k = (n-1)//15
    bagi3 = (3*(i+1)*i)//2
    bagi5 = (5*(j+1)*j)//2
    bagi15 = (15*(k+1)*k)//2
    sum = bagi3 + bagi5 - bagi15
    print(sum) 
    

    
    
    
    
    
    
    
    
    
    
    