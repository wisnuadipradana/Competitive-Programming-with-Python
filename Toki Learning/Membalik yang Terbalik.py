# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

x, y = input().split()

x_balik = ''.join(reversed(x))
y_balik = ''.join(reversed(y))
jumlah = int(x_balik)+int(y_balik)
jumlah_balik = ''.join(reversed(str(jumlah)))

print(int(jumlah_balik))