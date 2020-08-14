# Enter your code here. Read input from STDIN. Print output to STDOUT

def mean(val_list,n):
    return sum(val_list)/n

def median(val_list,n):
    val_list.sort()
    if(n%2==0):
        return (val_list[int(n/2)]+val_list[int(n/2 - 1)])/2
    else:
        return val_list[int(n/2)]

def mode(val_list,n):
    val_count={}
    mode_max=0
    mode=val_list[0]
    for val in val_list:
        if val in val_count:
            val_count[val]+=1
        else:
            val_count[val]=1
        
        if val_count[val]>mode_max:
            mode_max=val_count[val]
            mode=val

    return mode

if __name__ == "__main__":
    n=int(input())
    values = list(map(int,input().rstrip().split()))
    print(mean(values,n))
    print(median(values,n))
    print(mode(values,n))
