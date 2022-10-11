# -*- coding: utf-8 -*-
"""
@author: uzumakinagato
"""

angka = int(input())

def factor(angka):
    faktor = []
    i = 1
    while i <= angka:
        if angka%i == 0:
            faktor.append(int(angka/i))
        i +=1
    return faktor

def primeornot(angka):
    banyaknya_faktor = 0
    for i in range(2,int(angka**.5)+1):
        if angka%i == 0:
            banyaknya_faktor += 1
    if angka==1:
        return False 
    if banyaknya_faktor==0 : 
        return True
    else :
        return False

def primefactor(angka):
    faktorprima = []
    for k in factor(angka):
        if primeornot(k)==True:
            faktorprima.append(k)
    return sorted(faktorprima)

def powers_factorization(angka):
    pangkat_faktorprima = []
    for k in primefactor(angka):
        pangkat = 0
        M = angka
        while M%k == 0:
            pangkat += 1
            M //= k
        pangkat_faktorprima.append(pangkat)
    return pangkat_faktorprima

faktor_prima = primefactor(angka)
pangkat_faktorisasiprima = powers_factorization(angka)

if pangkat_faktorisasiprima[0] == 1:
    print(faktor_prima[0])
else:
    print('{}^{}'.format(faktor_prima[0],pangkat_faktorisasiprima[0]), end='')
for i, j in zip(faktor_prima[1:], pangkat_faktorisasiprima[1:]):
    if j==1:
        print(' x {}'.format(i), end='')
    else:
        print(' x {}^{}'.format(i,j), end='')