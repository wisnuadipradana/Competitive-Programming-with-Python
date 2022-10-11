# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:33:10 2020

@author: uzumakinagato
"""

'''
m,n = input().split()
m = int(m) ; n = int(n)

isibaris = []
for _ in range(m):
    baris = list(map(int, input().split()))
    isibaris.append(baris)


#dua dimensi
if len(baris) == n: 
    print('\n'.join([' '.join(['{:n}'.format(isibaris[m-i-1][j]) for i in range(m)]) for j in range(n)]))  
    
'''  

m,n = input().split()
m = int(m); n = int(n)

matriks = []
for i in range(m):
    baris = input().split()
    if len(baris) == n:
        for j in range(n):
            baris[j] = int(baris[j])
        matriks.append(baris) 

matriks_baru = []

for i in range(n):
    baris_baru = []
    for j in range(m):
        baris_baru.append(matriks[m-j-1][i])
    matriks_baru.append(baris_baru)

for baris in matriks_baru :
    for i in range(m-1):
        print(baris[i],end=" ")
    print(baris[m-1])  














'''

rotasibaris = []
if len(baris) == n:
    for j in range(n):
        for i in range(m):
            print('{:n}'.format(isibaris[m-i-1][j]))   
 #           rotasibaris.append(isibaris[m-i-1][j])
#    print(rotasibaris) 




#satu dimensi

if len(baris) == n:
    list = []
    for x in isibaris:
        for y in range(n):
            list.append(x[y])  

    for j in range(0,n,-1):
        for i in range(m):
            print(list[(m-j)*n+i])
'''        
    
'''
 0   1    2    3  ...  n-1
 n  n+1  n+2  n+3 ... 2n-1
2n 2n+1 2n+2 2n+3 ... 3n-1
3n 3n+1 3n+2 3n+3 ... 4n-1
.
.
.
(m-3)n (m-3)n+1 (m-3)n+2 (m-3)n+3 ... (m-2)n-1
(m-2)n (m-2)n+1 (m-2)n+2 (m-2)n+3 ... (m-1)n-1
(m-1)n (m-1)n+1 (m-1)n+2 (m-1)n+3 ...    mn-1

  (m-1)n   (m-2)n   (m-3)n  ...  3n   2n   n  0
(m-1)n+1 (m-2)n+1 (m-2)n+1  ... 3n+1 2n+1 n+1 1
(m-1)n+2 (m-2)n+2 (m-2)n+2  ... 3n+2 2n+2 n+2 2
.
.
.
    mn-1 (m-1)n-1 (m-2)n-1  ... 4n-1 3n-1 2n-1 n-1


'''

