# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 00:47:44 2020

@author: uzumakinagato
"""



def PythagoreanTriplet(N): 
    arr = []
    for a in range(1,(N//3)+1):
        for b in range(a+1,(N//2)+1): 
            c = N-a-b 
            if(a*a + b*b == c*c): 
                print(N, "=", a, b, c, end = "=") 
                arr.append(a*b*c)           
    if len(arr) == 0 :
        print(-1) 
    else :
        print(max(arr)) 



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    PythagoreanTriplet(n)   


'''
def Pythagoreantriplet(N):
    arr = []
    if N%2 == 0:
        K = N//2
        for m in range(2,K): 
            p = K//m
            if K%m == 0 and p>m and 2*m>p:
                a = m**2-(p-m)**2
                b = 2*m*(p-m)
                c = m**2+(p-m)**2
                print(N,a,b,c,sep=",") 
                arr.append(a*b*c)
    if len(arr) == 0 :
        print(-1) 
    else :
        print(max(arr))        


for i in range(101): 
    Pythagoreantriplet(i)    
'''

# 12 24 30 '36 40 48 56 60 70 '72 80 84 90 96, 50 100