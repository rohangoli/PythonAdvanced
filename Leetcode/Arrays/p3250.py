## Check If N and Its Double Exist

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

# Example 2:
# Input: arr = [7,1,14,11]
# Output: true
# Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

# Example 3:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: In this case does not exist N and M, such that N = 2 * M.

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        N=len(arr)
        i=0
        while i<N:
            j=0
            while j<N:
                if i!=j and arr[i]*2==arr[j]:
                    return True
                j+=1
            i+=1
            
        return False