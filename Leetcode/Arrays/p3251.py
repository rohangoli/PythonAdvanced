## Valid Mountain Array

# Example 1:
# Input: arr = [2,1]
# Output: false

# Example 2:
# Input: arr = [3,5,5]
# Output: false

# Example 3:
# Input: arr = [0,3,2,1]
# Output: true

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N=len(arr)
        
        if N<=2:
            return False
        
        maxIdx = 0
        i=1
        while i<N:
            if arr[i]>arr[maxIdx]:
                maxIdx=i
            i+=1
            
        if not 0<maxIdx<N-1:
            return False
        
        i=0
        while i<maxIdx:
            if not arr[i]<arr[i+1]:
                return False
            i+=1
        
        i=N-1
        while i>maxIdx:
            if not arr[i]<arr[i-1]:
                return False
            i-=1
            
        return True