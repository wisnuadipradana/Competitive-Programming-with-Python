# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

S, T = input().split()

while T in S:
    S = ''.join([i for i in S.partition(T) if T!=i])
print(S)