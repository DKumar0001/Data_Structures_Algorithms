#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    size = len(arr)
    for i in range(0,size):
        while(arr[i] != i+1):
            count+=1
            swap = arr[arr[i]-1]
            arr[arr[i]-1] = arr[i]
            arr[i] = swap
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
