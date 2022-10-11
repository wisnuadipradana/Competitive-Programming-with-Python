# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:45:18 2020

@author: uzumakinagato
"""
'''

def prime(x):
    if x ==1:
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
ii
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(n,0,-1): 
        if n%i == 0 and prime(i) == True:
            print(i)
            break
'''

def max_prime_factor(x): 
    maxPrime = -1

    while x % 2 == 0: 
        maxPrime = 2
        x >>= 1 # equivalent to n //= 2
    
    for i in range(3, int(x**.5) + 1, 2): 
        while x % i == 0: 
            maxPrime = i 
            x //= i 
    
    return x if x > 2 else maxPrime
  

t = int(input().strip())
for _ in range(t): 
    n = int(input().strip())
    print(max_prime_factor(n))
