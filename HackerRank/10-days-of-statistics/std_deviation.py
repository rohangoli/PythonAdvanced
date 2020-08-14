# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def mean(val_list,n):
    return sum(val_list)/n

def std_dev(val_list,n):
    mn = mean(val_list,n)
    stddev = math.sqrt(sum([(x-mn)**2 for x in val_list])/n)
    return stddev

if __name__ == "__main__":
    n=int(input())
    values = list(map(int,input().rstrip().split()))
    print("%.1f"%(std_dev(values,n)))
