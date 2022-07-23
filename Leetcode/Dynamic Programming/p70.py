## 70. Climbing Stairs

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n==1 or n==2:
            return n
        
        dp = {}
        
        def helper(x):
            if x==1 or x==0:
                return 1
            
            if (x-1) not in dp:
                dp[x-1] = helper(x-1)
            if (x-2) not in dp:
                dp[x-2] = helper(x-2)
                
            dp[x] = dp[x-1]+dp[x-2]
            
            return dp[x]
            
        helper(n)
        
        return dp[n]
        
#         self.total = 0
#         def helper(inc):
#             if inc==n:
#                 self.total+=1
#                 return None
#             elif inc>n:
#                 return None
#             else:
#                 return helper(inc+1) or helper(inc+2)
            
#         helper(0)
#         return self.total