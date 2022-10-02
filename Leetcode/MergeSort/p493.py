## 493. Reverse Pairs

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # ## TC - O(N^2) SC - O(1)
        # result = 0
        # i=0
        # while i<len(nums)-1:
        #     j=i+1
        #     while j<len(nums):
        #         if nums[i]>nums[j]*2:
        #             result+=1
        #         j+=1
        #     i+=1
            
        # return result
    
        self.count = 0
        
        def revMergeSort(nums):
            if len(nums)>1:
                mid = len(nums)//2
                leftArr = nums[:mid]
                rightArr = nums[mid:]
                
                revMergeSort(leftArr)
                revMergeSort(rightArr)
                # print(leftArr, rightArr)
                
                i=j=0
                while i<len(leftArr) and j<len(rightArr):
                    if leftArr[i]>2*rightArr[j]:
                        self.count+= (len(rightArr)-j)
                        i+=1
                    else:
                        j+=1
                
                i=j=k=0
                while i<len(leftArr) and j<len(rightArr):
                    if leftArr[i]>rightArr[j]:
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
        
        # print(nums)
        revMergeSort(nums)           
        # print(nums)  

        return self.count
        