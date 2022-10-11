# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:05:27 2020

@author: uzumakinagato
"""


xsatu,ysatu,xdua,ydua = map(int, input().split())

if xsatu >= xdua:
    zsatu = xsatu - xdua
elif xsatu < xdua:
    zsatu = xdua - xsatu

if ysatu >= ydua:
    zdua = ysatu - ydua
elif ysatu < ydua:
    zdua = ydua - ysatu

print(zsatu+zdua)  
