# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 20:43:19 2020

@author: uzumakinagato
"""

def swap_case(s):  
    kata = ''
    for i in s:
        if i.islower() == True:
            kata += i.upper()
        elif i.isupper() == True:
            kata += i.lower()
        else :
            kata += i
    return kata
  
if __name__ == '__main__':
    s = input() 
    result = swap_case(s)
    print(result)
    print(s[1],s[2],s[11])  
    print(len(s))
    print(s.upper())
    print(s.lower())
    print(s.count("a"))  
    print(s.find("kucing"))
    print(s.replace("kucing","meong"))