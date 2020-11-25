#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0;
    if(len(s)>n):
        for i in range(0,n):
            if (s[i] == 'a'):
                count+=1
    else:
        for i in range(0, len(s)):
            if(s[i]=='a'):
                count+=1
        repeat = n//len(s)
        count = count * repeat
        rem = n%len(s)
        for i in range(0,rem):
            if s[i] == 'a':
                count+=1
    return count
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
