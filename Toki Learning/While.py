# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 00:58:11 2020

@author: uzumakinagato
"""
kucing = 0

while kucing < 1:
    try:
        x = input()
    except EOFError:
        break
    print(x) 
     
