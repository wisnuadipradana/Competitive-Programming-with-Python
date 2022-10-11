# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 23:55:28 2020

@author: uzumakinagato
"""

import sys

def LCM(x,y):
    a = x; b = y
    z = -1
    if x < y :
        while z != 0 :
            z =  y - (y//x)*x  
            y = x  
            x = z  
        return (a*b)//y
    elif x > y :
        while z != 0 :
            z =  x - (x//y)*y  
            x = y  
            y = z    
        return (a*b)//x
    elif x == y :
        return (a*b)//x

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    p = 1
    for i in range(1,n+1):
        m = LCM(i,p) 
        p = m 
    print(m)    
