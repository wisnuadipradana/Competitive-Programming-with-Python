# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 00:19:50 2020

@author: uzumakinagato
"""

'''
kucing = 0
N = int(input())

if N==1:
    print("ya")
else :
    while kucing ==0 :
        if N %2 == 0 :
            N /= 2
            if N == 1: 
                print("ya")
                break
        else :
            print("bukan")
            break
'''

'''
N = int(input())

if N==1 :
    print("ya")
else :
    for i in range(100):
        if N%2 == 0:
            N/= 2
            if N==1:
                print("ya")
                break
        else:
            print("bukan")
            break
'''


'''
N = int(input())
    
for i in range(100):
    if N%2 ==0:
        N /=2

if N == 1:
    print("ya")
else:
    print("bukan")
'''

kucing = 0
N = int(input())

while kucing==0:
    if N%2 == 0:
        N /= 2
    else :
        break

if N == 1:
    print("ya")
else:
    print("bukan")  


    
