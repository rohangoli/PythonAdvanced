## 125. Valid Palindrome

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        tempS = []
        for x in s:
            temp = ord(x)
            if 65<=temp<=90:
                temp = temp+32
            temp = chr(temp)
            if temp.isalnum():
                tempS.append(temp)
                
        print(tempS)
        i=0
        j=len(tempS)-1
        while i<j:
            if tempS[i]!=tempS[j]:
                return False
            i+=1
            j-=1
        return True