# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 12:07:25 2020

@author: uzumakinagato
"""

def namescores(nama):
    sum = 0
    for i in nama:
        if i.isupper() == True :  
            sum += ord(i)-64
        elif i.islower() == True :
            sum += ord(i)-96
    return sum 

listnama = []
t = int(input().strip())
for a0 in range(t):
    name = input().strip()
    listnama.append(name)

listnama.sort() 

Q = int(input().strip())
for a0 in range(Q):
    jeneng = input().strip() 
    for i in range(t):
        if jeneng in listnama[i]:
            print((i+1)*namescores(jeneng))  
            

    