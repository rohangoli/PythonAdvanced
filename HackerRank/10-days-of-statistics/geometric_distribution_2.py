# Enter your code here. Read input from STDIN. Print output to STDOUT

def geometric_distribution(n,p):
    q=1-p
    return q**(n-1)*p

s=0
p=1/3
for i in range(1,6):
    s+= geometric_distribution(i,p)

print("%.3f"%s)
