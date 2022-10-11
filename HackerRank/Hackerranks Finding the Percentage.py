# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:16:40 2020

@author: uzumakinagato
"""


if __name__ == '__main__':
    n = int(input()) 
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


for nama in list(student_marks.keys()):
    if nama == query_name: 
        total = 0
        for x in student_marks[query_name]:
            total += x

print(float(total/3)) 
