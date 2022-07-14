## 1047. Remove All Adjacent Duplicates In String

# Example 1:
# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

# Example 2:
# Input: s = "azxxzy"
# Output: "ay"

class Solution:
    def removeDuplicates(self, s: str) -> str:
        tempS = []
        
        for x in s:
            if tempS and tempS[-1]==x:
                while tempS and tempS[-1]==x:
                    tempS.pop()
            else:
                tempS.append(x)
            
        return ''.join(tempS)