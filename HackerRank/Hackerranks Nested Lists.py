# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:34:33 2020

@author: uzumakinagato
"""


if __name__ == '__main__':
    data = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list = [score,name]
        data.append(list)

skor = []
for k in range(len(data)):
    skor.append(data[k][0])
print(skor)

listskor = []
for isi in skor:
    if isi not in listskor:
        listskor.append(isi)
listskor.sort() 
print(listskor)


second = listskor[1]
nama = []
for i in range(len(data)):
    if data[i][0] == second: 
        nama.append(data[i][1]) 
print(nama)
nama.sort() 
for jeneng in nama:
    print(jeneng) 
    
'''
5
Harsh
20
Beria
20
Varun
19
Kakunami
19
Vikas
21
'''

'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
'''