## LKP '18 Contest 2 P1 - Food Lines

(n,m) = map(int, input().split())
lines = list(map(int, input().split()))

def find_shortline(ll):
    shortest = 0
    i=1
    while i<len(ll):
        if ll[i]<ll[shortest]:
            shortest=i
        i+=1
    return shortest

j=0
while j<m:
    minIdx = find_shortline(lines)
    print(lines[minIdx])
    lines[minIdx]+=1
    j+=1