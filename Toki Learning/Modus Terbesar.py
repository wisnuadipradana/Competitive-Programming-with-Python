# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 01:02:08 2020

@author: uzumakinagato
"""

import statistics
import scipy.stats

N = int(input())
 
lists = list(map(int, input().split())) 

lists.sort(reverse=True) 
 
'''               
listnodouble = []
for isi in lists:
    if isi not in listnodouble:
        listnodouble.append(isi)
listnodouble.sort()
'''

maks = max((lists.count(item), item) for item in lists)[1]
print(maks)

#modus = scipy.stats.mode(lists)

#print(statistics.multimode(lists))
#print(lists.index(modus)) 

#print(modus[0][0])        


'''
listnodouble = list(set(lists))   
maks = max(listnodouble)

for i,j in enumerate(listnodouble):
    



banyakkembar = []
for isi in listnodouble:
    kembar = lists.count(isi)
    banyakkembar.append(kembar)
 
modus = banyakkembar[0]
for i in range(1,len(banyakkembar)):
    if modus < banyakkembar[i]:
        modus = banyakkembar[i]

for i in range(len(listnodouble)):
    if modus == banyakkembar[i]:
        a = i  
print(listnodouble[i]) 
'''  