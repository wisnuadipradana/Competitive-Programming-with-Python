# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 16:44:55 2020

@author: uzumakinagato
"""


import scipy.stats

t = int(input().strip())
n = list(map(int, input().strip().split(' ')))   
n.sort()

print(round(sum(n)/len(n), 1))
print(round((n[(t-1)//2]+n[t//2])/2, 1))
modus = scipy.stats.mode(n, axis= None)[0][0]
print(round(modus, 1))  

