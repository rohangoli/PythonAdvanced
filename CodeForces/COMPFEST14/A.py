## A. Accumulation of Dominoes

(r,c) = map(int,input().split())
if r>c:
    print((r-1)*c)
else:
    print((c-1)*r)