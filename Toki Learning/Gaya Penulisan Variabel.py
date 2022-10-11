# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

S = input()

if "_" in S:
    S_baru = S.split('_')[0]
    for i in S.split('_')[1:]:
        S_baru += i.capitalize()
    print(S_baru)
else:
    S_baru = ''
    for i in S:
        if i.isupper()==True:
            S_baru += '_'+i.lower()
        else:
            S_baru += i
    print(S_baru)