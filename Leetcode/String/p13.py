## 13. Roman to Integer

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0
        i=0
        N=len(s)
        while i<N:
            temp = maps[s[i]]
            if i+1<N:
                if s[i:i+2]=='IV':
                    temp=4
                    i+=1
                if s[i:i+2]=='IX':
                    temp=9
                    i+=1
                if s[i:i+2]=='XL':
                    temp=40
                    i+=1
                elif s[i:i+2]=='XC':
                    temp=90
                    i+=1
                elif s[i:i+2]=='CD':
                    temp=400
                    i+=1
                elif s[i:i+2]=='CM':
                    temp=900
                    i+=1
            result +=temp
            i+=1
        return result