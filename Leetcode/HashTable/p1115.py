## Two Sum

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        temp={}
        # i=0
        # while i<len(nums):
        #     if target-nums[i] not in temp:
        #         temp[nums[i]]=i
        #     else:
        #         return [temp[target-nums[i]],i]
        #     i+=1
        
        for idx,num in enumerate(nums):
            diff = target-num
            if diff in temp:
                return temp[diff],idx
            temp[num]=idx
        
        
        # nums.sort()
        # print(nums)
        # i=0
        # j=len(nums)-1
        # tempSum=0
        # while i<j:
        #     tempSum = nums[i]+nums[j]
        #     print(i,j,nums[i],nums[j],tempSum,target)
        #     if tempSum>target:
        #         j-=1
        #     elif tempSum<target:
        #         i+=1
        #     else:
        #         print('-'*25)
        #         return [i,j]
        # print('-'*25)