# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 00:35:31 2020

@author: uzumakinagato
"""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    listarr = list(arr)

if len(listarr) == n:
    listarrsort = sorted(listarr)
    daftar = []
    for isi in listarrsort:
        if isi not in daftar:
            daftar.append(isi)
    daftar.reverse()
    print(daftar[1]) 