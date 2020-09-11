# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def binary_distribution(x,n,p):
    q=1-p
    return nCr(n,x)*(p**x)*(q**(n-x))

p=109/209
s=0
for i in range(3,7):
    s+= binary_distribution(i,6,p)

print("%.3f"%(s))

