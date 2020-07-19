#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minval = maxval = scores[0]
    minchg = maxchg = 0
    for val in scores:
        if val>maxval:
            maxval = val
            maxchg+=1

        if val<minval:
            minval=val
            minchg+=1

    return [maxchg,minchg]

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))

