#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    a_length = len(a)
    count = 0
    for i in range(0,a_length):
        for j in range(0, n-i-1):
            if(a[j]>a[j+1]):
                a[j+1],a[j] = a[j], a[j+1]
                count+=1
    print("Array is sorted in {:d} swaps.\nFirst Element: {:d}\nLast Element: {:d}\n".format(count,a[0],a[a_length-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
