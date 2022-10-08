## Subarray with given sum

def subArraySum(arr, n, s): 
    #Write your code here
    currSum = arr[0]
    left = 0
    right = 1
    while right<=n:
        while currSum>s and left<right:
            currSum -= arr[left]
            left+=1
            
        if currSum == s:
            return left+1, right
        
        if right<n:
            currSum += arr[right]
        right+=1
    
    return -1

def subArraySum_V2(arr, n, s): 
    #Write your code here
    currSum = arr[0]
    left = 0
    right = 1
    while right<=n:
        while currSum>s and left<right-1:
            currSum -= arr[left]
            left+=1
            
        if currSum == s:
            return left+1, right
        
        if right<n:  
            currSum += arr[right]
        right+=1
    
    return -1

test_cases = [
    ([1,2,3,4,5,6,7,8,9,10,11],11,12),
    ([1,2,3,4,5,6,7,8,9,10,11],11,10),
    ([1,2,3,4,5,6,7,8,9,10,11],11,15),
    ([1,2,3,4,5,6,7,8,9,10,11],11,18),
    ([1,2,3,4,5,6,7,8,9,10,11],11,9),
    ([135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 196, 143, 28, 37, 192, 5, 103,
     154, 93, 183, 22, 117, 119, 96, 48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134],42,468), # 38 42
    ([1,2,3,7,5],5,12),
    ([1,2,3,7,5],5,10),
    ([1,2,3,7,5],5,15),
    ([1,2,3,7,5],5,24),
]

for x,y,z in test_cases:
    print(subArraySum(x,y,z))