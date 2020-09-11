# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def poisson_distribution(l,k):
    return l**k * math.exp(-l) / math.factorial(k)

print("%.3f"%(poisson_distribution(2.5,5)))
