#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    elements = len(a)
    num_rot = d % elements
    while(num_rot >0):
        swap = a[0]
        for i in range(0, elements-1):
            a[i] = a[i+1]
        a[elements-1] = swap
        num_rot-=1;
    return a
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
