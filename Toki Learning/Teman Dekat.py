# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

from itertools import combinations

Input = list(map(int, input().split()))
N = Input[0]; D = Input[1]

X = []; Y = []
for i in range(N):
    X_, Y_ = list(map(int, input().split()))
    X.append(X_)
    Y.append(Y_)

T_ij = lambda x_i,x_j,y_i,y_j: abs(x_j-x_i)**D+abs(y_j-y_i)**D

T = []
for k in combinations(range(N),2):
    T.append(T_ij(X[k[0]],X[k[1]],Y[k[0]],Y[k[1]]))

print(min(T), max(T))    