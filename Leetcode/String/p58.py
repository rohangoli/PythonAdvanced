## Length of Last Word

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        N = len(s)
        
        i=N-1
        while i>=0 and s[i]==' ':
            i-=1
        
        result = 0
        while i>=0 and s[i]!=' ':
            result +=1
            i-=1
            
        return result