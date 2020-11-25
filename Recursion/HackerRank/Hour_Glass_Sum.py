#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = -10000
    current_sum = 0
    length = 6
    width = 6
    for i in range(1, length-1):
        for j in range(1, width-1):
            current_sum = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]+ arr[i][j] + arr[i+1][j-1] + arr[i+1][j] +arr[i+1][j+1]
            if(current_sum > max_sum):
                max_sum = current_sum
    return max_sum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
