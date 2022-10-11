# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:48:47 2020

@author: uzumakinagato
"""

import sys

def faktorial(x):
   if x == 1 :
       return 1
   else :
       return (x*faktorial(x-1))   

arr = []
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')  
    n,k = [int(n),int(k)]
    m = faktorial(n+k)//(faktorial(n)*faktorial(k))
    hasil = m%(10**9 +7)
    print(hasil) 
    