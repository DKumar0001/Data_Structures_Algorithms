#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate
# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # n, m = map(int, input().split())
    a = [0] * (n+1)
    m_sum = temp =0
    for i in range(len(queries)):
        f,l,val = queries[i][0], queries[i][1], queries[i][2]
        a[f-1] += val
        if l<=n:
            a[l] -= val
    for i in a:
        temp+=i
        if(m_sum < temp):
            m_sum = temp
    return m_sum
            
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
