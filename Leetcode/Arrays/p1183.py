## Reverse String

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        N=len(s)
        
        i=0
        j=N-1
        
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
            
        return s