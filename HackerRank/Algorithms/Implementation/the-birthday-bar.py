#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    combinations=0
    
    #print(len(s)-m+1)
    for i in range(len(s)-m+1):
        #print(d,s[i:i+m])
        if(d==sum(s[i:i+m])):
            combinations+=1

    return combinations

if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    print(str(result) + '\n')
