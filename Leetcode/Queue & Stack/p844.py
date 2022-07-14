## 844. Backspace String Compare

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        tempS1 = []
        for x in s:
            if tempS1 and x=='#':
                tempS1.pop()
            elif x=='#':
                continue
            else:
                tempS1.append(x)
                
        tempS2 = []
        for x in t:
            if tempS2 and x=='#':
                tempS2.pop()
            elif x=='#':
                continue
            else:
                tempS2.append(x)  
        print(tempS1, tempS2)        
        return tempS1==tempS2