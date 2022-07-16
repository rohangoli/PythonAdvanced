## 709. To Lower Case

# Example 1:
# Input: s = "Hello"
# Output: "hello"

# Example 2:
# Input: s = "here"
# Output: "here"

# Example 3:
# Input: s = "LOVELY"
# Output: "lovely"

class Solution:
    def toLowerCase(self, s: str) -> str:
        N = len(s)
        i=0
        result = []
        while i<N:
            temp = ord(s[i])
            print(temp)
            if 65<=temp<=90:
                temp = temp+32
            result.append(chr(temp))
            i+=1
        return ''.join(result)