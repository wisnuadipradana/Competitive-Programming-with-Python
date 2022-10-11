# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:29:53 2020

@author: uzumakinagato
"""


N = int(input())

list = []
for i in range(N):
    kata = input().split() 
    if kata[0] == 'insert' :
        list.insert(int(kata[1]),int(kata[2]))
    if kata[0] == 'print' :
        print(list) 
    if kata[0] == 'remove' :
        list.remove(int(kata[1])) 
    if kata[0] == 'append' :
        list.append(int(kata[1])) 
    if kata[0] == 'sort' :
        list.sort()           
    if kata[0] == 'pop' :
        list.pop()
    if kata[0] == 'reverse' :
        list.reverse()
    