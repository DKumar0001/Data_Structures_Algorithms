#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    hashWords = {}
    for m_words in magazine:
        if(hashWords.get(m_words) != None):
            if (hashWords[m_words] > 0):
                hashWords[m_words] += 1
        else:
            hashWords[m_words] = 1   
    for r_word in note:
        if hashWords.get(r_word) is None or hashWords[r_word] == 0:
            print("No")
            return
        else:
            hashWords[r_word] -= 1
    print("Yes")
    
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
