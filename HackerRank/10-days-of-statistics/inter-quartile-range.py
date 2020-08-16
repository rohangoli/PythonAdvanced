# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

def median(val_list):
    n=len(val_list)
    val_list.sort()
    if(n%2==0):
        return (val_list[int(n/2)]+val_list[int(n/2 - 1)])/2
    else:
        return val_list[int(n/2)]


if __name__ == "__main__":
    n=int(input())
    pvalues=list(map(int,input().rstrip().split()))
    frequency=list(map(int,input().rstrip().split()))
    
    values=[]
    for i,f in enumerate(frequency):
        values.extend([pvalues[i]]*f)
    values.sort()
    mid=int(len(values)/2)
    q1=median(values[:mid])
    q2=median(values)
    if(n%2==0):
        q3=median(values[mid:])
    else:
        q3=median(values[mid+1:])
    print("%.1f"%(q3-q1))
