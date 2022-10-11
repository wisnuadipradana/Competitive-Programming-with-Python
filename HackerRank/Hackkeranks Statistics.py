# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 01:28:10 2020

@author: uzumakinagato
"""

n = int(input())

a = list(map(int, input().strip().split(' ')))

mean = sum(a)/len(a)

var = sum([(i-mean)**2 for i in a])/len(a)

std = var**.5

print(round(std, 1))

a.sort()
print(a) 

def Median(x, List):
    if x % 2 != 0:
        median_ = List[(x-1)//2]
    else:
        median_ = (List[x//2-1] + List[x//2])/2
    return int(median_)
 
    
if n%2== 0:
    print(Median(n//2, a[:n//2])) 
    print(Median(n, a)) 
    print(Median(n//2, a[n//2:])) 
else :
    print(Median(n//2, a[:n//2])) 
    print(Median(n, a)) 
    print(Median(n//2, a[n//2+1:])) 






'''
from statistics import median
n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
t=int(len(arr)/2)
if len(arr)%2==0:
    L=arr[:t]
    U=arr[t:]
else:
    L=arr[:t]
    U=arr[t+1:]
    
print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))

'''




'''
3 5 7 8 12 13 14 18 21 
'''
   