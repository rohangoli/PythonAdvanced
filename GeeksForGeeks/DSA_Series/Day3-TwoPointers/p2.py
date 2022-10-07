## Count Triplets with sum smaller than X

def countTriplets(arr, n, sumo):
    #code here
    arr.sort()
    result = 0 
    # i=0
    # k=n-1
    # while i<k:
    #     tempSum = arr[i]+arr[k]
    #     j=i+1
    #     while j<k:
    #         if (tempSum+arr[j])<sumo:
    #             result+=1
    #         j+=1
    #     k-=1
    i=0
    while i<n-2:
        j=i+1
        k=n-1
        while j<k:
            if (arr[i]+arr[j]+arr[k])>=sumo:
                k-=1
            else:
                result+=(k-j)
                j+=1
        i+=1
        
    return result

test_cases = [
    ([-2, 0, 1, 3],4,2),
    ([5, 1, 3, 4, 7],5,12),
    ([5, 1, 3, 4, 7, 0, 2],7,7)
    ]
for x,y,z in test_cases:
    print(countTriplets(x,y,z))