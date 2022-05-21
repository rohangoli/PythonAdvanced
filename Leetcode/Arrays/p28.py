## Implement strStr()

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        M = len(haystack)
        N = len(needle)
        
        if N==0:
            result=0
        else:
            result=-1
        
        i=0
        while i<M-N+1:
            if needle == haystack[i:i+N]:
                result=i
                break
                
            i+=1
            
        return result