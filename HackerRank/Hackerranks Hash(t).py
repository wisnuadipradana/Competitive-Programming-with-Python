# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 01:05:33 2020

@author: uzumakinagato
"""

if __name__ == '__main__':
    n = int(input()) 
    integer_list = tuple(map(int, input().split()))

print(integer_list) 
print(hash((integer_list))) 
