# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 00:04:04 2020

@author: uzumakinagato
"""


kucing = 0
jumlah = 0
while kucing == 0 :
    try:
        x = int(input())
    except EOFError:
        break
    jumlah += x
print(jumlah)




