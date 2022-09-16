import math

def partition(nums, left, right):
    pivot = nums[left]
    i,j = left, right

    while i<j:
        while(nums[i]<=pivot):
            i+=1
        
        while(nums[j]>pivot):
            j-=1

        if i<j:
            nums[i],nums[j] = nums[j],nums[i] 
    
    nums[j],nums[left] = nums[left], nums[j]

    return j
    # pivotIdx = left

    # while left<right:
    #     while nums[left]<nums[pivotIdx]:
    #         left+=1

    #     while nums[right]>nums[pivotIdx]:    
    #         right-=1
        
    #     if left<right:
    #         nums[left],nums[right] = nums[right],nums[left]                        

    # nums[pivotIdx],nums[left] = nums[left], nums[pivotIdx]

    # return left

def quickSort(nums, left, right):
    if left<=right:
        partition_position = partition(nums,left, right)

        quickSort(nums,left, partition_position-1)
        quickSort(nums,partition_position+1,right)


tc = [[5,3,1,5,8,9],[1,6,0,1,3,8,2,4],[1,3,0,7,-1,5,-10,20]]
for idx,arr in enumerate(tc):
    arr.append(math.inf)
    print("TestCase: {}\nGiven Array: {}".format(idx,arr))
    quickSort(arr,0,len(arr)-1)
    arr[-1:]=[]
    print("Sorted Array: ",arr)