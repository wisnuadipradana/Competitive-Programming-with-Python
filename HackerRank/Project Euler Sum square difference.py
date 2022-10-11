# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 02:57:14 2020

@author: uzumakinagato
"""

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) 
    print(((n-1)*n*(n+1)*(3*n+2))//12)


