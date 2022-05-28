## Jewels and Stones

# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0

from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        temp=Counter()
        for x in stones:
            temp[x]+=1
        # print(temp)
        result=0
        for k,v in temp.items():
            if k in jewels:
                result+=v
                
        return result