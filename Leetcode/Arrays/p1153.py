##  Two Sum II - Input array is sorted

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        
        # N=0
        # while numbers[N]<target and N<M-1:
        #     N+=1
        # N+=1
        # print(N)
        
        # i=0
        # while i<N:
        #     j=i+1
        #     while j<N:
        #         if numbers[i]+numbers[j]==target:
        #             return [i+1,j+1]
        #         j+=1
        #     i+=1
        
        i=0
        j=N-1
        while i<N:
            temp = numbers[i]+numbers[j]
            if temp<target:
                i+=1
            elif temp>target:
                j-=1
            else:
                return [i+1,j+1]
        