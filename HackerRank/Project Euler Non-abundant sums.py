# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:08:52 2020

@author: uzumakinagato
"""


def abundantnumber(x):
    sum = 0
    for i in range(1,x):
        if x%i == 0:
            sum += i
    if sum > x :
        return True
    else :
        return False

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    list = []
    if n > 28123 :
        print('YES')
    else :
        for i in range(n+1):
            if abundantnumber(i) == True :
                list.append(i)
        listabundant = []
        for j in list:
            for k in list:
                listabundant.append(j+k)
        if n in listabundant:
            print('YES')
        else :
            print('NO') 
    
    