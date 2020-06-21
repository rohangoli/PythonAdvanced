from math import gcd
from functools import reduce

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

def gcdl(multiples):
    result=multiples[0]
    for mult in multiples:
        result=gcd(result,mult)
    return result

def getTotalX(arr,brr):
    count=0
    f=lcm(arr)
    l=gcdl(brr)
    i=f
    j=2
    while(i<=l):
        if(l%i==0):
            count+=1
        i=f*j
        j+=1
    return count
    return (f,l)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print(str(total) + '\n')
