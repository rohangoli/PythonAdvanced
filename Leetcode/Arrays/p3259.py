## Replace Elements with Greatest Element on Right Side

# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

# Example 2:
# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N=len(arr)
        
        if N==1:
            return [-1]
        
        i=0
        maxIdx=i
        while i<N-1:
            
            if i<maxIdx:
                arr[i]=arr[maxIdx]
                i+=1
                continue
                
            if i==maxIdx:
                maxIdx=i+1
            
            j=i+1
            while j<N:
                if arr[j]>arr[maxIdx]:
                    maxIdx=j
                j+=1
            
            arr[i]=arr[maxIdx]
            
            i+=1
            
        arr[-1]=-1
        
        return arr

    def replaceElements_Fast(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        max_val = -1
        for i in range(n-1, -1, -1):
            arr[i], max_val = max_val, max(max_val, arr[i])
        
        return arr
            