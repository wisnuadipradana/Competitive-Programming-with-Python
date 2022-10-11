# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

from itertools import combinations

N, K = input().split()
N = int(N); K = int(K)

for i in combinations(range(1, N+1), K):
    for j in i:
        print(j, end=' ')
    print('')

