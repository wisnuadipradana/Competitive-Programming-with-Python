# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = int(input())

switch = []
for i in range(M):
    M = input().split()
    M[1] = int(M[1])
    M[3] = int(M[3])
    switch.append([M[0],M[1],M[2],M[3]])
    
for isi in switch:
    if isi[0]=='A' and isi[2]=='B':
        k = A[isi[1]-1]
        A[isi[1]-1] = B[isi[3]-1]
        B[isi[3]-1] = k
    if isi[0]=='B' and isi[2]=='A':
        k = B[isi[1]-1]
        B[isi[1]-1] = A[isi[3]-1]
        A[isi[3]-1] = k
    if isi[0]=='A' and isi[2]=='A':
        k = A[isi[1]-1]
        A[isi[1]-1] = A[isi[3]-1]
        A[isi[3]-1] = k
    if isi[0]=='B' and isi[2]=='B':
        k = B[isi[1]-1]
        B[isi[1]-1] = B[isi[3]-1]
        B[isi[3]-1] = k

for i in A[:-1]:
    print(i, end=' ')
print(A[-1])
for j in B:
    print(j, end=' ')