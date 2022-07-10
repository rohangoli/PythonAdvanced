## Sqrt(x)

# Example 1:
# Input: x = 4
# Output: 2

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        
        # if x==0 or x==1:
        #     return x
        
        left = 0
        right = x
        while left<=right:
            mid = left + (right-left)//2
            if mid**2 > x:
                right = mid-1
            else:
                left = mid+1
            
        return left-1