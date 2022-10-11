# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

S = input()
K = int(input())

S_baru = ''
for i in S:
    if ord(i)+K>122:
        S_baru += chr(ord(i)+K-26)
    else:
        S_baru += chr(ord(i)+K)
print(S_baru)