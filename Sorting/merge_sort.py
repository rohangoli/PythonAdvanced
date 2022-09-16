def mergeSort(nums):
    if len(nums)>1:
        mid = len(nums)//2

        L_nums = nums[:mid]
        R_nums = nums[mid:]

        mergeSort(L_nums)
        mergeSort(R_nums)

        i=j=k=0
        while i<len(L_nums) and j<len(R_nums):
            if L_nums[i]<R_nums[j]:
                nums[k] = L_nums[i]
                i+=1
            else:
                nums[k] = R_nums[j]
                j+=1
            k+=1

        while i<len(L_nums):
            nums[k] = L_nums[i]
            i+=1
            k+=1
        while j<len(R_nums):
            nums[k] = R_nums[j]
            j+=1
            k+=1
    # return nums

tc = [[5,3,1,5,8,9],[1,6,0,1,3,8,2,4],[1,3,0,7,-1,5,-10,20]]
for idx,arr in enumerate(tc):
    print("TestCase: {}\nGiven Array: {}".format(idx,arr))
    mergeSort(arr)
    print("Sorted Array: ",arr)