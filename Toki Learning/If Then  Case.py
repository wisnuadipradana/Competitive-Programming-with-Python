# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 15:36:49 2020

@author: uzumakinagato
"""


N = int(input())

if 1<=N<=9:
    print('satuan')
elif 10<=N<=99:
    print('puluhan')
elif 100<=N<=999:
    print('ratusan')
elif 1000<=N<=9999:
    print('ribuan')
elif 10000<=N<=99999:
    print('puluhribuan')

    