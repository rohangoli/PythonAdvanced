## Perfect Squares

# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

import math
class Solution:
    def numSquares(self, n: int) -> int:
        nums = [(_)**2 for _ in range(math.floor(math.sqrt(n)),0,-1)]
        if nums[0]==n:
            return 1
        
        tempQ = [0]
        visited = set()
        visited.add(0)
        level = 0
        while tempQ:
            # print(level, tempQ)
            size = len(tempQ)
            
            for i in range(size):
                curr = tempQ.pop(0)
            
                if curr==n:
                    return level
                
                for x in nums:
                    temp = x+curr
                    if temp not in visited and temp<=n:
                        tempQ.append(temp)
                        visited.add(temp)
                        
            level+=1
                
        return 0
            
            
            
        