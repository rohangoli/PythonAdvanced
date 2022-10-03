## 344. Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        ## In-Place Recursion
        def helper(arr, low=0, high=None):
            if not high:
                high = len(arr)-1   
            if high<=low:
                return arr
            arr[low], arr[high] = arr[high], arr[low]
            return helper(arr,low+1, high-1)
        
        return helper(s)
        
        ## Swapping In-Place
        # N=len(s)
        # i=0
        # j=N-1
        # while i<j:
        #     s[i],s[j]=s[j],s[i]
        #     i+=1
        #     j-=1  
        # return s
        