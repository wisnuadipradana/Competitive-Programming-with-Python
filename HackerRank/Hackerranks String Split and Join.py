# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:34:09 2020

@author: uzumakinagato
"""

def split_and_join(line):
    split = line.split(' ')
    join = "-".join(split)
    return join 

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result) 