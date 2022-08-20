## 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ## Selection Sort
        # for i in range(len(nums)):
        #     minIdx = i
        #     for j in range(i+1,len(nums)):
        #         if nums[j]<nums[minIdx]:
        #             minIdx=j           
        #     nums[i],nums[minIdx] = nums[minIdx], nums[i]
        
        ## Counting Sort
        K = max(nums)
        counts = [0]*(K+1)
        for x in nums:
            counts[x]+=1
        #print(counts)
        startIdx = 0
        for idx, count in enumerate(counts):
            counts[idx] = startIdx
            startIdx +=count
        #print(counts) 
        sorted_nums = [0]*len(nums)
        for num in nums:
            print(sorted_nums)
            sorted_nums[counts[num]] = num
            counts[num]+=1
        #print(sorted_nums) 
        i=0
        while i<len(nums):
            nums[i]=sorted_nums[i]
            i+=1