# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:27:06 2020

@author: uzumakinagato
"""

def fibonacci(x):
    phi = (1+(5)**.5)/2
    phi_inverse = -1/phi
    return int((phi**(x+1) - phi_inverse**(x+1))/(5)**.5) 
'''
def Fibonacci(x):
    if x ==1 :
        return 1
    elif x == 2 :
        return 2
    else :
        return Fibonacci(x-1)+Fibonacci(x-2) 
'''
list = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    list.append(n)
    i = 2; hasil = 0
    while fibonacci(i) < n:
        hasil += fibonacci(i) 
        i += 3  
    print((fibonacci(i-1)-1)//2)
    print(hasil) 

    
'''
1,2,3,5,8,13,21,34,55,89,144,...
1,2,3,4,5, 6,7, 8, 9, 10, 11,...

'''