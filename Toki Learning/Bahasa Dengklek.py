# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

S = input()

S_baru = ''
for i in S:
    if i.isupper()==True:
        S_baru += i.lower()
    if i.islower()==True:
        S_baru += i.upper()
print(S_baru)