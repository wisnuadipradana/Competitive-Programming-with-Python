# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:24:52 2020

@author: uzumakinagato
"""

def fibonacci(x):
    phi = (1+(5)**.5)/2
    phi_inverse = -1/phi
    return int((phi**x - phi_inverse**x)/(5)**.5) 
    
'''
def Fibonacci(x):
    if x ==1 :
        return 1
    elif x == 2 :
        return 1
    else :
        return Fibonacci(x-1)+Fibonacci(x-2) 
'''


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 1
    while True:
        x = fibonacci(i)
        if len(str(x)) == n:
            print(i)
            break
        i += 1
