## Equilibrium Point

def equilibriumPoint(A, N):
    # Your code here
    total = sum(A)
    
    i=0
    rtot = 0
    while i<N:
        if rtot == total-A[i]-rtot:
            return i+1
        rtot+=A[i]
        i+=1
    return -1

test_cases = [([1,3,5,2,2],5), ([1],1),([1,3,1],3),([1,3,4,9,6,1,1],7),([1,3,4,9,6,1],6)]
for x,y in test_cases:
    print(equilibriumPoint(x,y))