# Enter your code here. Read input from STDIN. Print output to STDOUT

def weighted_mean(val_1,val_2,n):
    return sum([val_1[i]*val_2[i] for i in range(n)])/sum(val_2)

if __name__ == "__main__":
    n=int(input())
    values_1 = list(map(int,input().rstrip().split()))
    values_2 = list(map(int,input().rstrip().split()))
    print("%.1f"%weighted_mean(values_1,values_2,n))
