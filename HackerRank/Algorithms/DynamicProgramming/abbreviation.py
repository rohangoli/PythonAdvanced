#!/bin/python3

import math
import os
import random
import re
import sys

remove_lower = lambda text: re.sub('[a-z]', '', text)
# Complete the abbreviation function below.
def abbreviation(a, b):
    if(len(a)<len(b)):
        return "NO"
    elif(b in remove_lower(a)):
        return "YES"
    else:
        i=0
        while(i<len(a)):
            if(97<=ord(a[i])<=122):
                break
            i +=1
        if(i<len(a)):
            return abbreviation(a[:i]+a[i].upper()+a[i+1:],b)
        else:
            return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
