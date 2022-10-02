## 775. Global and Local Inversions

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        def revMergeSort(nums):
            if len(nums)>1:
                mid = len(nums)//2
                leftArr = nums[:mid]
                rightArr = nums[mid:]
                
                revMergeSort(leftArr)
                revMergeSort(rightArr)

                i=j=k=0
                while i<len(leftArr) and j<len(rightArr):
                    if leftArr[i]>rightArr[j]:
                        self.count+= (len(rightArr)-j)
                        nums[k]=leftArr[i]
                        k+=1
                        i+=1
                    else:
                        nums[k]=rightArr[j]
                        k+=1
                        j+=1
                        
                while i<len(leftArr):
                    nums[k]=leftArr[i]
                    k+=1
                    i+=1
                    
                while j<len(rightArr):
                    nums[k]=rightArr[j]
                    j+=1
                    k+=1
        revMergeSort(nums)           
        return self.count   
    
    def isIdealPermutation(self, nums: List[int]) -> bool:
        local_invs = global_invs = 0
        
        ## TLE - TC - O(N)
        i=0
        while i<len(nums):
            if abs(i-nums[i])>1:
                return False
            i+=1
        return True
        
        ## TLE - TC - O(N.LogN + N)
        i=0
        while i<len(nums)-1:
            if nums[i]>nums[i+1]:
                local_invs+=1
            i+=1
        
        global_invs = self.reversePairs(nums)
        
        return local_invs==global_invs