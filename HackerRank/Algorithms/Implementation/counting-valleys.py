#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    prev = '-'
    ind = 0
    val_count=0
    curr_level = 0
    while(ind<n):
        if(s[ind]=='U'):
            print('/',sep=' ')
            curr_level+=1
        else:
            print('\\',sep=' ')
            curr_level-=1

        if curr_level==0 and s[ind]=='U':
            print('-',sep=' ')
            val_count+=1

        ind+=1
        
    return val_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

