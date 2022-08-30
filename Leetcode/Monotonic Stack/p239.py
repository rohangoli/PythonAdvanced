## 239. Sliding Window Maximum

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=r=0
        output=[]
        tempQ = deque()
        while r<len(nums):
            #print(l,r,tempQ)
            ## pop smaller values from Queue
            while tempQ and nums[tempQ[-1]]<nums[r]:
                tempQ.pop()
            tempQ.append(r)
            
            ## Remove left Val from window
            if l>tempQ[0]:
                tempQ.popleft()
            
            if (r+1)>=k:
                #print(tempQ)
                output.append(nums[tempQ[0]])
                #print(output)
                l+=1
                
            r+=1
            
        return output
            