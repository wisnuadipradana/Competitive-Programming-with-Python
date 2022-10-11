# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

N = int(input())

def dec_to_biner(x):
    simpan = []
    while x>1:
        simpan.append(x%2)
        x = x//2
    simpan.append(x)
    return int("".join(map(str, simpan[::-1])))

print(dec_to_biner(N))