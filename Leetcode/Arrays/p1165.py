## Reverse Words in a String III

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"

class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        i=0
        while i<len(temp):
            temp[i]=temp[i][::-1]
            i+=1
        return " ".join(temp)