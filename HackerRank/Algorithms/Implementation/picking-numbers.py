#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    diff0 = 0
    diff1 = 0
    maxpick = 0
    for x in a:
        diff0=a.count(x)
        diff1=a.count(x-1)
        diff0+=diff1
        if diff0>maxpick:
            maxpick=diff0
    
    return maxpick

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

