# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

S = input()

def cek_palindrom(s):
    if len(s)>1:
        if s[0]==s[-1]:
            return cek_palindrom(s[1:-1])
        else:
            return 'BUKAN'
    else:
        return 'YA'
    
print(cek_palindrom(S))