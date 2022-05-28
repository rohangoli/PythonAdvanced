## Longest Substring Without Repeating Characters

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        ## O(N^2) - Rohan's solution
        N=len(s)
        maxLen=0
        substrings=()
        i=0
        while i<N:
            temp=set()
            j=i
            while j<N and s[j] not in temp:
                temp.add(s[j])
                # print(temp)
                j+=1
                
            if len(s[i:j])>maxLen:
                maxLen=j-i
            # print(s[i:j],maxLen)
            i+=1
        # print('-'*25)
        return maxLen

    def lengthOfLongestSubstring_v2(s: str) -> int:
        ## O(N) - solution from Leetcode
        # Base condition
        if s == "":
            return 0
        # Starting index of window
        start = 0
        # Ending index of window
        end = 0
        # Maximum length of substring without repeating characters
        maxLength = 0
        # Set to store unique characters
        unique_characters = set()
        # Loop for each character in the string
        while end < len(s):
            if s[end] not in unique_characters:
                unique_characters.add(s[end])
                end += 1
                maxLength = max(maxLength, len(unique_characters))
            else:
                unique_characters.remove(s[start])
                start += 1
        return maxLength