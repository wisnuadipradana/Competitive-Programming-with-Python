# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 01:45:33 2020

@author: uzumakinagato
"""


N = int(input())
data = map(int, input().split())
arr = list(data)

if len(arr) == N :
    maxmin = sorted(arr)
    print(maxmin[N-1], maxmin[0])

