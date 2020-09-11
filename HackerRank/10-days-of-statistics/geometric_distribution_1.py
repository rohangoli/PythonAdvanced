# Enter your code here. Read input from STDIN. Print output to STDOUT

def geometric_distribution(n,p):
    q=1-p
    return q**(n-1)*p

print("%.3f"%(geometric_distribution(5,1/3)))

