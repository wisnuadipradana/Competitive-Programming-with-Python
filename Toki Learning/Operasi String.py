# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

S1 = input()
S2 = input()
S3 = input()
S4 = input()

K = ''.join(S1.split(S2))
K_baru = ''
for i in K.partition(S3):
    if i==S3:
        K_baru += i+S4
    else:
        K_baru += i
print(K_baru)