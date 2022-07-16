## 1528. Shuffle String

# Example 1:
# Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
# Output: "leetcode"
# Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

# Example 2:
# Input: s = "abc", indices = [0,1,2]
# Output: "abc"
# Explanation: After shuffling, each character remains in its position.

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        N = len(indices)
        temp = [None]*N
        
        i=0
        while i<N:
            temp[indices[i]] = s[i]
            i+=1
            
        return ''.join(temp)