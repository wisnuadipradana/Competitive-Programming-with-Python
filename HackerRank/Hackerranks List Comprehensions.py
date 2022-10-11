# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:34:01 2020

@author: uzumakinagato
"""


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())


list = []
for x in range(x+1):
    for y in range(y+1):
        for z in range(z+1):
            if x+y+z != n:
                lst = [x,y,z] 
#                lst = [[x,y,z] for i in range(1)]
                list.append(lst)   

print(list)
