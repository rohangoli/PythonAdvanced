# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

p=12/100

def binary_distribution(x,n,p):
    q=1-p
    return nCr(n,x)*(p**x)*(q**(n-x))

s=0
for i in range(0,3):
    s+= binary_distribution(i,10,p)

print("%.3f"%s)

s=0
for i in range(2,11):
    s+= binary_distribution(i,10,p)

print("%.3f"%s)

