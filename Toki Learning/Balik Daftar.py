# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 00:58:26 2020

@author: uzumakinagato
"""


daftar = []
while True:
    try:
        x = int(input())
    except EOFError:
        break
    daftar.append(x)
daftar.reverse() 
for i in daftar:
    print(i)