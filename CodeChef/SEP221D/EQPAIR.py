# cook your dish here
from collections import Counter
tempHM = {}
def gcd(a,b):
    if b==0:
        return a
    elif (a,b) in tempHM:
        return tempHM[(a,b)]
    else:
        tempHM[(a,b)] = gcd(b,a%b)
        return tempHM[(a,b)]

def sumN(x):
    return x*(x+1)/2
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    result = 0
    tempC = Counter(a)
    for k,v in tempC.items():
        #print(k,v,sumN(v-1))
        result+=sumN(v-1)
            
    # for i in range(n-1):
    #     for j in range(i+1,n):
    #         tempg = gcd(a[i],a[j])
    #         #print(a[i],a[j],tempg)
    #         if tempg**2==(a[i]*a[j]):
    #             result+=1
    print(int(result))
