#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    ans = 0
    state = 0
    elements = len(q)
    for i in range(elements-1, 0,-1):
        if(q[i] - i > 3):
            state = 1
        for j in range(max(0, q[i]-2), i):
            if(q[j] > q[i]):
                ans+=1
    switch ={
        1: "Too chaotic",
        0 : ans
    }
    print(switch[state])
    
        
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
