# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:50:06 2020

@author: uzumakinagato
"""


x = float(input())
y = int(x)

if x == y:
    print(y, y,sep=' ')
else:
    if x>0:
        print(y, y+1,sep=' ')
    elif x<0:
        print(y-1, y,sep=' ') 
