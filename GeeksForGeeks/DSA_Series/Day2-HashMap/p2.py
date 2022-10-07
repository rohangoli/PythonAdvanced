## SubArray range with given sum

def subArraySum(arr, n, sum):
    #Your code here
    prefixSums = {0:1}
    
    i=0
    tempSum = 0
    result = 0
    while i<n:
        tempSum+=arr[i]
        diff = tempSum-sum
        
        result+=prefixSums.get(diff,0)
        
        prefixSums[tempSum] = 1 + prefixSums.get(tempSum, 0)
            
        i+=1
        
    return result

test_cases = [([10,2,-2,-20,10],5,-10),([1,4,20,3,10,5],6,33)]
for x,y,z in test_cases:
    print(subArraySum(x,y,z))