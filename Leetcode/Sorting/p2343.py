## Query Kth Smallest Trimmed Number

class Solution:
    def counting_sort(self, nums: List[str], place_val:int, K:int=10) -> None:
        counts = [0]*K
        for num in nums:
            digit = (num//place_val)%10
            counts[digit]+=1

        startIdx = 0
        for idx, count in enumerate(counts):
            counts[idx] = startIdx
            startIdx +=count

        sorted_nums = [0]*len(nums)
        for num in nums:
            digit = (num//place_val)%10
            sorted_nums[counts[digit]] = num
            counts[digit]+=1

        #return sorted_nums
        i=0
        while i<len(nums):
            nums[i]=sorted_nums[i]
            i+=1
            
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
#         nums[:] = [int(num) for num in nums]
#         actual = nums.copy()
#         #shift = min(nums)
#         #nums[:] = [num-shift for num in nums]
#         max_elem = max(nums)
        
#         place_val = 1
#         trim_place = 1
#         tempHM = {}
#         while place_val < max_elem:
#             self.counting_sort(nums, place_val)
#             tempHM[trim_place] = nums.copy() #[num+max_elem for num in nums]
#             trim_place+=1
#             place_val*=10
            
#         #print(tempHM)
        
#         result = []
#         for k,trim in queries:
#             #print(k,trim,tempHM[trim][k-1])
#             result.append(actual.index(tempHM[trim][k-1]))
#         #     print(tempHM[trim], 10**(trim-1))
#         #     #print(tempHM[trim][k-1], 10**(trim-1))
#         #     result.append((tempHM[trim][k-1]//(10**(trim-1)))%10)
        
#         return result

        # TC - O (Q * N * LogN)
        result = []
        for k,t in queries:
            arr = []
            for i,x in enumerate(nums):
                arr.append((int(x[-t:]),i))
            #print(arr)
            arr.sort()
            result.append(arr[k-1][1])
            
        return result
                
        