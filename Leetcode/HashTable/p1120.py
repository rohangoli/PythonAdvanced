## First Unique Character in a String

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp={}
        for x in s:
            if x in temp:
                temp[x]+=1
                continue
            temp[x]=1
        # print(temp)
        
        result=-1
        for k,v in temp.items():
            if v==1:
                result = s.index(k)
                break
                
        return result