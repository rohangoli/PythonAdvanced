## Heap Sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def max_heapify(heap_size, index):
            largest = index
            left = index*2 + 1
            right = index*2 + 2
            if left<heap_size and nums[left]>nums[largest]:
                largest = left
            if right<heap_size and nums[right]>nums[largest]:
                largest = right
                
            if largest!=index:
                nums[largest], nums[index] = nums[index], nums[largest]
                max_heapify(heap_size, largest)
        #print(nums)        
        for i in range(len(nums)//2-1,-1,-1):
            max_heapify(len(nums),i)
            
        #print(nums)
        for i in range(len(nums)-1, 0,-1):
            nums[0], nums[i] = nums[i], nums[0]
            max_heapify(i, 0)
        
        return nums