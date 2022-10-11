# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 17:31:20 2021

@author: uzumakinagato
"""
from collections import Counter
from itertools import groupby

n = int(input())

l = list(map(int, input().split()))
freqs = groupby(Counter(l).most_common(), lambda x:x[1])

print(max([val for val,count in next(freqs)[1]]))