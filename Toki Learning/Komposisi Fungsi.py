# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

n = list(map(int, input().split()))

f = lambda x: abs(n[0]*x+n[1])

komposisi = n[3]
for i in range(n[2]):
    komposisi = f(komposisi)
print(komposisi)