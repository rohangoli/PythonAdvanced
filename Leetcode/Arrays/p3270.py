##  Find All Numbers Disappeared in an Array

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N=len(nums)
        
        temp=[False]*N
        i=0
        j=N-1
        while i<=j:
            temp[nums[i]-1]=True
            temp[nums[j]-1]=True
            #print(i,j,temp)
            i+=1
            j-=1
        
        i=0
        result=[]
        while i<N:
            if temp[i]==False:
                result.append(i+1)
            i+=1
        #print('-'*25)
        return result
        