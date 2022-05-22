## Duplicate Zeros

# Example 1:
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Example 2:
# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N=len(arr)
        zeros = 0
        i=0
        while i<N:
            if arr[i]==0:
                zeros+=1
            i+=1
            
        arr.extend([0]*zeros)
            
        i=N-1
        j=N+zeros-1
        while i>=0 and j>=0:
            if arr[i]!=0:
                arr[j]=arr[i]
                j-=1
            else:
                # Assign 2 zeros at zero'th element
                arr[j],arr[j-1]=0,0
                j-=2
            i-=1
            # print(arr)
        # arr=arr[:N]
        arr[N:]=[]
        # print(arr)