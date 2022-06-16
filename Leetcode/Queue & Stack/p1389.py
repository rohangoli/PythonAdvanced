## Target Sum

# Example 1:
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# Example 2:
# Input: nums = [1], target = 1
# Output: 1


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        ## Dynamic Programming
        ## https://leetcode.com/problems/target-sum/discuss/2137338/python-simple-solutions
        dp={}
        
        def helper(idx,val):
            if idx==len(nums):
                if val==target:
                    return 1
                return 0
            
            if (idx,val) in dp:
                return dp[(idx,val)]
            
            dp[(idx,val)] = helper(idx+1, val+nums[idx]) + helper(idx+1, val-nums[idx])
            
            return dp[(idx,val)]
            
        return helper(0,0)
        
        result = 0 
        
        if not nums:
            return result
        
        ## Recursive DFS - Working & Not Submitting
        def helper(idx, val):
            if idx==len(nums):
                if val==target:
                    nonlocal result
                    result+=1
                return
            
            helper(idx+1, val+nums[idx])
            helper(idx+1, val-nums[idx])
            
        helper(0,0)
        
        return result
        
        # BFS - Time Limit Exceeded
        queue = [0]
        result = 0
        idx = 0   
        while queue and idx<=len(nums):
            size = len(queue)
            print(idx, queue)
            for _ in range(size):
                curr = queue.pop(0)
                if curr == target and idx==len(nums):
                    result+=1
                    
                if idx>=len(nums):
                    continue
                    
                temp1, temp2 = curr+nums[idx], curr-nums[idx]
                queue.append(temp1)
                queue.append(temp2)
                        
            idx+=1
                    
        return result