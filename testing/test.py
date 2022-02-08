#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'filterBadWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING badWords
#  2. STRING message
#
import re
punc = {'\'', '.', '"', '!', ')', '(', '?', ','}

def removePuncuation(word):
    for p in punc:
        word = word.replace(p, '')
    return word
def filterBadWords(badWords, message):
    # Write your code here
    # setter = set(badWords.split(' '))
    # new_message = message.split(' ')
    # print(setter)
    # for i in range(len(new_message)):
    #     print(new_message[i])
    #     if str(new_message[i]) in setter:
    #         new_message[i] = '*' * len(new_message[i])
            
    # return " ".join(new_message)
    regex_bad_words = [ ('^' + x.replace('*', '.*') + '$', x.replace('*', '')) for x in badWords.split(' ')]
    new_message = message.split(' ') 
    for i in range(len(new_message)):
        word = new_message[i]
        word = word.lower()
        word = removePuncuation(word)
        for reg, bad in regex_bad_words:
            if bool(re.match(reg, word)):
                print(re.match(reg, word))
                index = new_message[i].lower().index(bad)
                replace = [x for x in new_message[i]]
                for j in range(len(replace)):
                    if replace[j] not in punc: replace[j] = '*'
                new_message[i] = ''.join(replace)
                break
    return ' '.join(new_message)
                    
            
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    badWords = input()

    message = input()

    result = filterBadWords(badWords, message)

    fptr.write(result + '\n')

    fptr.close()
