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
    values=list(map(int,input().rstrip().split()))
    values.sort()
    mid=int(n/2)
    q1=median(values[:mid])
    q2=median(values)
    if(n%2==0):
        q3=median(values[mid:])
    else:
        q3=median(values[mid+1:])
    print("%g\n%g\n%g"%(q1,q2,q3))
