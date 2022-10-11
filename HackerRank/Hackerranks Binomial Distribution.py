# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:01:59 2020

@author: uzumakinagato
""" 

def faktorial(x):
    return 1 if x==1 else x*faktorial(x-1)

def kombinasi(n, x):
    return faktorial(n)/(faktorial(n-x)*faktorial(x))

def Binom(n, x, p):
    return kombinasi(n, x) * p**x *(1-p)**(n-x)

l, r = list(map(float, input().strip().split(' ')))
m = r/(l+r)
sum = 0
for i in range(3,7):
    sum += Binom(6, i, m)
print("%.3f" %sum) 

