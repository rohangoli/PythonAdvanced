# https://dmoj.ca/problem/cco07p2
# CCO '07 P2 - Snowflakes

## TC - O(N^2) - TLE
## Use HashMap key as sum of snowflake lengths to identify possible buckets for comparisons

def identical_right(sf1, sf2, start):
    for offset in range(6):
        if sf1[offset]!=sf2[(start+offset)%6]:
            return False
    return True

def identical_left(sf1, sf2, start):
    for offset in range(6):
        indx2 = start-offset
        if indx2<0:
            indx2 +=6
        if sf1[offset]!=sf2[indx2]:
            return False
    return True

def are_identical(sf1, sf2):
    for start in range(6):
        if identical_right(sf1, sf2, start):
            return True
        if identical_left(sf1, sf2, start):
            return True
    return False    

def identify_identical(values, n):
    i=0
    while i<n-1:
        j=i+1
        while j<n:
            if(are_identical(values[i],values[j])):
                print("Twin snowflakes found.")
                return True
            j+=1
        i+=1
    
    print("No two snowflakes are alike.")
    return False

N = int(input())
snow_flakes = []
for _ in range(N):
    snow_flakes.append(list(map(int,input().split())))

# print(N)
# print(snow_flakes)
identify_identical(snow_flakes,N)