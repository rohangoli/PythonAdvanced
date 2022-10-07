## Pair with given sum in a sorted array

def Countpair (arr, n, sum) : 
    #Complete the function
    result_pairs = []
    i=0
    j=n-1
    
    while i<j:
        tempSum = arr[i]+arr[j]
        if tempSum==sum:
            result_pairs.append((i,j))
            i+=1
            j-=1
        elif tempSum>sum:
            j-=1
        else:
            i+=1
            
    if result_pairs:
        return len(result_pairs)
    else:
        return -1

test_cases = [
    ([1, 2, 3, 4, 5, 6, 7],7,8),
    ([1, 2, 3, 4, 5, 6, 7],7,33),
    ([0,1, 2, 3, 4, 5, 6, 7],8,7)
    ]
for x,y,z in test_cases:
    print(Countpair(x,y,z))