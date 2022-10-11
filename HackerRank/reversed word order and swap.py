# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 03:37:22 2020

@author: uzumakinagato
"""

#sentence = 'Awesome IS Coding aS U MeAn uH'
def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split(' ')  
    reverse_sentence = ' '.join(reversed(words))  
    return reverse_sentence.swapcase() 
    
if __name__ == '__main__':
    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)
    print(result) 
    


'''

def reverse_words_order_and_swap_cases(sentence):
    space = []
    for i,j in enumerate(sentence):
        if j == ' ':
            space.append(i)

    space.reverse()
    if len(space) == 0:
        return sentence.swapcase() 
    else :
        print(sentence[space[0]+1:], end=' ') 
        for k in range(1,len(space)):
            print(sentence[space[k]+1:space[k-1]], end=' ') 
        print(sentence[:space[-1]])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
    
'''