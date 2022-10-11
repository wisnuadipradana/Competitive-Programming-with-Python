# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:48:31 2021

@author: uzumakinagato
"""
#import numpy as np

ukuran = list(map(int, input().split()))
N = ukuran[0]
M = ukuran[1]
P = ukuran[2]

A = []
for i in range(N):
    matriks = list(map(int, input().split()))
    A.append(matriks)
    
B = []
for i in range(M):
    matrik = list(map(int, input().split()))
    B.append(matrik) 

result = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

for isi in result: 
    for i in isi:
        print(i, end=' ')
    print('')

'''
print(np.array(A))
print(np.array(B)) 
    
C = np.array(A)@np.array(B)
for isi in C:
    for i in isi:
        print(i, end=' ')
    print('')
'''  


