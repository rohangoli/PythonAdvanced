## Reverse Words in a string

# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution:    
    def reverseWords(self, s: str) -> str:
        # N=len(s)
        
        temp = []
        for x in s.split():
            if x!='':
                temp.append(x)
        
        return " ".join(temp[::-1])