# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 23:35:45 2020

@author: uzumakinagato
"""
N = int(input())

isi = list(map(int, input().strip().split(' ')))
f =  list(map(int, input().strip().split(' ')))

S = []
for i in range(len(isi)):
    for j in range(f[i]):
        S.append(isi[i]) 

S.sort()

def Median(x, List):
    if x % 2 != 0:
        median_ = List[(x-1)//2]
    else:
        median_ = (List[x//2-1] + List[x//2])/2
    return round(median_, 1)

n = sum(f) 

if n%2== 0:
    Q1 = Median(n//2, S[:n//2])
    Q3 = Median(n//2, S[n//2:])
    print(round(float(Q3-Q1), 1))
    
else :
    Q1 = Median(n//2, S[:n//2])
    Q3 = Median(n//2, S[n//2+1:])
    print(round(float(Q3-Q1), 1)) 




