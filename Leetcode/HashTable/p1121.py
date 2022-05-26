## Contains Duplicate II

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [1,0,1,1], k = 1
# Output: true

# Example 3:
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## O(N^2)
        # temp={}
        # for idx, num in enumerate(nums):
        #     if num not in temp:
        #         temp[num]=[idx]
        #         continue
        #     temp[num].append(idx)
            
        # for x in temp:
        #     N=len(temp[x])
        #     i=0
        #     while i<N-1:
        #         if abs(temp[x][i]-temp[x][i+1])<=k:
        #             return True
        #         i+=1
                
        # return False

        ## O(N)
        temp={}
        for idx, num in enumerate(nums):
            if num in temp and idx-temp[num]<=k:
                return True
            temp[num]=idx
        return False